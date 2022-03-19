from django.contrib import admin

from core.models import *

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['name', 'cik_number']

@admin.register(RevenueFiling)
class RevenueFilingAdmin(admin.ModelAdmin):
    search_fields = ['company__name', 'company__cik_number']