# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Administradormodel(models.Model):

    #__Administradormodel_FIELDS__
    admin_cnpj = models.IntegerField(null=True, blank=True)

    #__Administradormodel_FIELDS__END

    class Meta:
        verbose_name        = _("Administradormodel")
        verbose_name_plural = _("Administradormodel")


class Fundosmodel(models.Model):

    #__Fundosmodel_FIELDS__
    fundo_ticker = models.CharField(max_length=255, null=True, blank=True)

    #__Fundosmodel_FIELDS__END

    class Meta:
        verbose_name        = _("Fundosmodel")
        verbose_name_plural = _("Fundosmodel")


class Rendimentosmodel(models.Model):

    #__Rendimentosmodel_FIELDS__
    admin_cnpj = models.ForeignKey(AdministradorModel, on_delete=models.CASCADE)
    fundo_cnpj = models.ForeignKey(FundosModel, on_delete=models.CASCADE)
    rendimento_database = models.DateTimeField(blank=True, null=True, default=timezone.now)
    rendimento_valor = models.IntegerField(null=True, blank=True)
    rendimento_datapgto = models.DateTimeField(blank=True, null=True, default=timezone.now)
    rendimento_periodoref = models.CharField(max_length=255, null=True, blank=True)

    #__Rendimentosmodel_FIELDS__END

    class Meta:
        verbose_name        = _("Rendimentosmodel")
        verbose_name_plural = _("Rendimentosmodel")



#__MODELS__END
