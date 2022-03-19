from rest_framework import serializers

from core.models import Company, RevenueFiling

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

class RevenueFilingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueFiling
        fields = "__all__"