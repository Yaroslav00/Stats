from django.urls import include, path
from rest_framework import routers
from stats.views import main_page

urlpatterns = [
    path('', main_page.as_view(), name='main_page')
]