from rest_framework import serializers
from core.models import *

class CustomCompanyField(serializers.RelatedField):

    # def to_representation(self, obj):
    #     return {
    #         'id': obj.id,
    #         'name': obj.name,
    #     }

    def to_internal_value(self, data):
        try:
            try:
                return Company.objects.get(name=data)
            except KeyError:
                raise serializers.ValidationError(
                    'id is a required field.'
                )
            except ValueError:
                raise serializers.ValidationError(
                    'id must be an integer.'
                )
        except Company.DoesNotExist:
            raise serializers.ValidationError(
            'Company does not exist.'
            )


class RevenueFilingPopulationSerializer(serializers.ModelSerializer):
    # company = serializers.CharField(source='company.name')
    # company = serializers.RelatedField(queryset=Company.objects.all())
    # company = serializers.ReadOnlyField(source='company.name')
    company = CustomCompanyField(queryset=Company.objects.all())
    
    class Meta:
        model = RevenueFiling
        fields = '__all__'


