from django.contrib import admin
from django.urls import path, include

from core.views import *

urlpatterns = [
    path('company/list/', CompanyList.as_view()),
    
    path('stats/revenue/<str:company_slug>/', RevenueStats.as_view())
]
