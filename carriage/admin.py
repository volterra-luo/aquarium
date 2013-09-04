#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from carriage.models import Group,Project,Transport,Tanker,Product

class GroupAdmin(admin.ModelAdmin):
    pass

class ProjAdmin(admin.ModelAdmin):
    pass

class TransportAdmin(admin.ModelAdmin):
    list_display = ['crg_id','tanker']

class TankerAdmin(admin.ModelAdmin):
    list_display = ['lpn','_category']

admin.site.register(Group,GroupAdmin)
admin.site.register(Project,ProjAdmin)
admin.site.register(Transport,TransportAdmin)
admin.site.register(Tanker,TankerAdmin)
admin.site.register(Product)