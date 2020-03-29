from django.urls import path
from . import views

app_name = 'iprocarlo_app'


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('new_search/', views.new_search, name='new_search'),

]
