from attr import field
from rest_framework import serializers

from core.models import *

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

class RevenueFilingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueFiling
        exclude = ['company']

class EbitdaFilingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EbitdaFiling
        exclude = ['company']