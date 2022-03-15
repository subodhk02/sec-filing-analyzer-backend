from django.contrib import admin
from django.urls import path, include

from core.views import *

urlpatterns = [
    path('company/list/', CompanyList.as_view())
]
