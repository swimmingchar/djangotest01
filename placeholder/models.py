# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class hostip(models.Model):
    ip_addr = models.GenericIPAddressField(u"IP地址", protocol="both", unpack_ipv4=False)
    root_signe = models.CharField(u"机房位置",max_length=50, blank=True)
    app_name = models.CharField(u"应用名",max_length=100, blank=True)
    
    # class Meta:
    #     verbose_name = _("hostip")
    #     verbose_name_plural = _("hostips")

    def __str__(self):
        return self.ip_addr

    # def get_absolute_url(self):
    #     return reverse("hostip_detail", kwargs={"pk": self.pk})

class relational(models.Model):
    source_app = models.CharField(u"源应用",max_length=100, blank=True)
    dest_app = models.CharField(u"目的应用",max_length=100, blank=True)
    app_relation = models.CharField(u"访问关系",max_length=15, blank=True)
    

    # class Meta:
    #     verbose_name = _("relational")
    #     verbose_name_plural = _("relationals")

    # def __str__(self):
    #     return self.source_app

    # def get_absolute_url(self):
    #     return reverse("relational_detail", kwargs={"pk": self.pk})
