from django.core.management.base import BaseCommand
from core.data_population.serializers import RevenueFilingPopulationSerializer
from core.providers.data_population import DataPopulationProvider

from core.models import Company, RevenueFiling

import json

class Command(BaseCommand):
    def handle(self, *args, **options):
        POPULATION_DATA = [
            (Company, None, 'core/data_population/company.json'),
            (RevenueFiling, RevenueFilingPopulationSerializer, 'core/data_population/revenue.json'),
        ]

        for data in POPULATION_DATA:
            model = data[0]
            serializer = data[1]
            file_path = data[2]

            with open(file_path) as f:
                data = json.load(f)
                provider = DataPopulationProvider(model=model, data=data, serializer=serializer)
                provider.populate()
        
        