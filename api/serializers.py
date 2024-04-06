from rest_framework import serializers
# from django.db import models
from api.models import State
from api.models import Country

# class CompanySerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Company
#         fields='__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields='__all__'

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model=State
        fields='__all__'

