from rest_framework import generics, filters
from core.models import *

from core.serializers import CompanySerializer, RevenueFilingSerializer

class CompanyList(generics.ListAPIView):
    serializer_class = CompanySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'cik_number']

    def get_queryset(self):
        return Company.objects.all()

class RevenueStats(generics.ListAPIView):
    serializer_class = RevenueFilingSerializer
    queryset = RevenueFiling.objects.all()
    
    def get_queryset(self):
        return super().get_queryset().filter(
            company__cik_number=self.kwargs['company_cik']
        )