from django.shortcuts import render
from rest_framework import viewsets
from api.models import State
from api.serializers import StateSerializer
from api.models import Country
from api.serializers import CountrySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
# class CompanyViewSet(viewsets.ModelViewSet):
#     queryset=State.objects.all()
#     serializer_class=StateSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset=Country.objects.all()
    serializer_class=CountrySerializer

    @action(detail=True,methods=['get'])
    def states(self,request,pk=None):
        try:
            Country=Country.objects.get(pk=pk)
            sta=State.objects.filter(Country=Country)
            sta_serializer=StateSerializer(sta,many=True,context={'request':request})
            return Response(sta_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':"Country might not exists !! Error"
            })

class StateViewSet(viewsets.ModelViewSet):
    queryset=State.objects.all()
    serializer_class=StateSerializer
