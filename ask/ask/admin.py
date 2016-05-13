#-*- coding: utf-8 -*-
from django.contrib import admin
from ask.models import Question
admin.site.register(Question)


#class askAdmin(admin.ModelAdmin):
#        fieldsets = []
#        admin.site.register(ask.askAdmin)
#