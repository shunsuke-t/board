from django.urls import path

from . import views

urlpatterns = [
    # path('', views.home, name='index'),
    path('', views.home, name='home'),
]
