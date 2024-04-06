from django.contrib import admin
from django.urls import path,include
from api.views import StateViewSet
from api.views import CountryViewSet
from rest_framework import routers

router=routers.DefaultRouter()
# router.register(r'companies',CompanyViewSet)
router.register(r'countries',CountryViewSet)
router.register(r'states',StateViewSet)



urlpatterns = [
    path('',include(router.urls))
]

# from django.urls import path
# from .views import CountryList

# urlpatterns = [
#     path('countries/', CountryList.as_view(), name='country-list'),
# ]
