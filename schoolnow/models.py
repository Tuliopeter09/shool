 # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import Permission, User
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver







class Mensagem(models.Model):
    created_by = models.ForeignKey(User, editable=False, default=1)

    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    memorando = models.CharField('', max_length=400)
    created_date = models.DateTimeField('Postado em:', default=timezone.now)

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
    #if created:
        #Mensagem.objects.create(created_by=instance)

#@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
#def save_user_profile(sender, instance, created, **kwargs):
    #user = instance
    #if created:
        #mensagem = Mensagem(created_by=user)
        #mensagem.save()

    
    def __str__(self):
        return self.memorando  




