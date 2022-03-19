from django.contrib import admin
from django.urls import path, include

from core.views import *

urlpatterns = [
    path('company/list/', CompanyList.as_view()),
    path('company/<str:slug>/', CompanyDetail.as_view()),
    
    path('stats/revenue/<str:company_slug>/', RevenueStats.as_view()),
    path('stats/ebitda/<str:company_slug>/', EbitdaStats.as_view())
]
