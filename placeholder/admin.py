# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from placeholder.models import hostip,relational

class hostipAdmin(admin.ModelAdmin):
    list_display = ('ip_addr',
                    'root_signe',
                    'app_name')
admin.site.register(hostip, hostipAdmin)

class relationalAdmin(admin.ModelAdmin):
    list_display = ('source_app',
                    'dest_app',
                    'app_relation')

admin.site.register(relational, relationalAdmin)



# Register your models here.
