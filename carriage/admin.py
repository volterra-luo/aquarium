#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from carriage.models import Group,Project,Transport

class GroupAdmin(admin.ModelAdmin):
    pass

class ProjAdmin(admin.ModelAdmin):
    pass

class TransportAdmin(admin.ModelAdmin):
    pass

admin.site.register(Group,GroupAdmin)
admin.site.register(Project,ProjAdmin)
admin.site.register(Transport,TransportAdmin)
