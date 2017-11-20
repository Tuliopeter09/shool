# -*- coding: utf-8 -*-


from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import UserForm, LoginForm, MensagemForm
from .models import User, Mensagem
from django.contrib.auth import login as auth_login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.core.urlresolvers import reverse


from django.shortcuts import render_to_response






def detail(request, mensagem_id):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        user = request.user
        mensagem = get_object_or_404(Mensagem, pk=mensagem_id)
        return render(request, 'schoolnow/detail.html', {'mensagem': mensagem, 'user': user})



def index(request):

        return render(request, 'schoolnow/index.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'schoolnow/index.html', context)


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('/criarmemorando')
            else:
                error = " Sorry! Username and Password didn't match, Please try again ! "
    else:
        form = LoginForm()
    return render(request, 'schoolnow/login.html', {"form":form})

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if User.objects.filter(email=instance.email).exists():
            messages.warning(request,
                            'Your email already exists in our database',
                            "alert alert-warning alert-dismissible")
        else:
            instance.save()
            messages.success(request,
                            'Your email has been submitted to the database',
                            "alert alert-success alert-dismissible")
            subject = "Obrigado por estar junto conosco!!"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            signup_message = '''Obrigado por se registrar no memorando SCHOOLNOW! Estamos bastante felizes e esperamos ver mensagens suas juntas a outros de milhares de participantes dessa ideia tão bacana! 
            Não se esqueça de nos seguir nas redes socias e de nos continuar acompanhando!! Aquele Beijão <3 '''
            #signup_message = render(request, 'plataforma/password_reset_email.html')
            #signup_message = render_to_response('plataforma/password_reset_email.html')

            send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=signup_message, fail_silently=False)

        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        #password = form.cleaned_data['password']

        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                memorandos = Mensagem.objects.filter(created_by=request.user)
                return render(request, 'schoolnow/bemvindo.html', {'memorandos': memorandos})
    context = {
        "form": form,
    }
    return render(request, 'schoolnow/register.html', context)


def bemvindo(request):

    if not request.user.is_authenticated():
        return render(request, 'schoolnow/bemvindo.html')
    else:
        template_name = 'schoolnow/bemvindo.html'
        model = Mensagem
        memorandos = Mensagem.objects.all().order_by('-created_date')
       #s User.objects.filter(groups__name='TURMA01')
        #all_forums = Forum.objects.all().order_by('-created_date')[:10]


       
    template = loader.get_template('schoolnow/bemvindo.html')
    #Forum.objects.filter(pergunta=id).order_by('pergunta')
    #Forum.objects.filter(id=id).order_by('-id') 
    #return all_forums


    context = {
        'memorandos': memorandos,
    }
    return HttpResponse(template.render(context, request))


    #entries = Forum.objects.all()[:20]
    return render_to_response('schoolnow/bemvindo.html')  

    
def criarmemorando(request):
    
    if not request.user.is_authenticated():
        return render(request, 'schoolnow/login.html')
    else:
        memorando_all= Mensagem.objects.all()
        model = Mensagem
     
        memorando_all = Mensagem.objects.all().order_by('-created_date')[:3]
        user_form = UserForm(request.POST, instance=request.user)


        form = MensagemForm(request.POST or None, request.FILES or None)
        if form.is_valid():

            fs= form.save(commit=False)
            #fs.user= request.user
            #created_by = Mensagem.objects.get(created_by=request.user)


            fs.created_by= request.user
            
            fs.save()

           
            memorando = form.cleaned_data['memorando']
            #created_by = form.cleaned_data['created_by']
            #created_date = form.cleaned_data['created_date']


            
            memorando = authenticate(memorando=memorando)
            #forum.save()

    context= {'form': form,
              'memorando_all': memorando_all,
              'user_form': user_form,

              }
    
    return render(request, 'schoolnow/criarmemorando.html', context)



def memorias(request):
    
    if not request.user.is_authenticated():
        return render(request, 'schoolnow/index.html')
    else:
        template_name = 'schoolnow/memorias.html'
        model = Mensagem
        memorando_all = Mensagem.objects.all().order_by('-created_date')
        #User.objects.filter(groups__name='TURMA01')
        user = User.objects.all()
        #all_forums = Forum.objects.all().order_by('-created_date')[:10]


        query = request.GET.get("q")
    if query:
        memorando_all = memorando_all.filter(memorando__icontains=query)

    template = loader.get_template('schoolnow/memorias.html')
    #Forum.objects.filter(pergunta=id).order_by('pergunta')
    #Forum.objects.filter(id=id).order_by('-id') 
    #return all_forums


    context = {
        'memorando_all': memorando_all,
    }
    return HttpResponse(template.render(context, request))


    #entries = Forum.objects.all()[:20]
    return render_to_response('schoonow/memorias.html')  


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'schoolnow/register.html', {'form': form})


def password_reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request, template_name='schoolnow/password_reset_confirm.html',
        uidb64=uidb64, token=token, post_reset_redirect=reverse('schoolnow:login_user'))


def reset(request):
    return password_reset(request, template_name='schoolnow/password_reset_form.html',
        email_template_name='schoolnow/password_reset_email.html',
        subject_template_name='schoolnow/password_reset_subject.txt',
        post_reset_redirect=reverse('schoolnow:login_user'))