from django.contrib import admin

from.models import *

# Register your models here.

# class catadmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('name',)}
#
#
admin.site.register(cartlist)
admin.site.register(item)
