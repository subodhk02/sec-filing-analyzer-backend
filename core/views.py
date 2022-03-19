from rest_framework import generics, filters
from core.models import *

from core.serializers import *

class CompanyList(generics.ListAPIView):
    serializer_class = CompanySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'slug', 'cik_number']

    def get_queryset(self):
        return Company.objects.all()

class RevenueStats(generics.ListAPIView):
    serializer_class = RevenueFilingSerializer
    queryset = RevenueFiling.objects.all()
    
    def get_queryset(self):
        return super().get_queryset().filter(
            company__slug=self.kwargs['company_slug']
        )

class EbitdaStats(generics.ListAPIView):
    serializer_class = EbitdaFilingSerializer
    queryset = EbitdaFiling.objects.all()
    
    def get_queryset(self):
        return super().get_queryset().filter(
            company__slug=self.kwargs['company_slug']
        )