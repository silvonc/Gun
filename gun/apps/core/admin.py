from django.contrib import admin

# admin.py - So you can see data in Django admin
from django.contrib import admin
from .models import Company, Contact

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'phone', 'created_at')
    list_filter = ('company',)
    search_fields = ('name', 'phone')
