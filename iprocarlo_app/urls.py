from django.urls import path
from . import views

app_name = 'iprocarlo_app'


urlpatterns = [
    path('', views.home, name='home'),
    path('new_search/', views.new_search, name='new_search'),
]
