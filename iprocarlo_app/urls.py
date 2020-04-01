from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# app_name = 'iprocarlo_app'


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('user/', views.user_page, name='user'),
    path('new_search/', views.new_search, name='new_search'),

    path(
        'reset_password/',
        auth_views.PasswordResetView.as_view(template_name='iprocarlo_app/password_reset.html'),
        name='reset_password'
    ),
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='iprocarlo_app/password_reset_sent.html'),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='iprocarlo_app/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(template_name='iprocarlo_app/password_reset_complete.html'),
        name='password_reset_complete'
    ),
]
