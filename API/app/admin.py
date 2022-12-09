from django.contrib import admin
from .models import Employee

# Register your models here.

class EmplyeeAdmin(admin.ModelAdmin):
    list_display = ['name','city','phone','salary','gender']
admin.site.register(Employee,EmplyeeAdmin)
