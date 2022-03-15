from rest_framework import generics
from core.models import Company

from core.serializers import CompanySerializer

class CompanyList(generics.ListAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        return Company.objects.all()