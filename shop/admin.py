from django.contrib import admin

# Register your models here.
from.models import *

# Register your models here.

class catadmin(admin.ModelAdmin):

    list_display=['name','slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(categ, catadmin)


class prodadmin(admin.ModelAdmin):

    list_display = ['name', 'slug','price','stock','img']
    list_editable = ['price','stock','img']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(products, prodadmin)
