from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView  
from authentication import views
from authentication.forms import  ResetPasswordConfirmForm, ResetPasswordForm
from .views import application_view, registrar_view, track_application, update_status  
from .views import download_pdf, download_word, download_excel



app_name = 'authentication'

urlpatterns = [
    
    path('application/<int:application_id>/download/pdf/', download_pdf, name='download_pdf'),
    path('application/<int:application_id>/download/word/', download_word, name='download_word'),
    path('application/<int:application_id>/download/excel/', download_excel, name='download_excel'),

    
    path('login/', views.login_view, name='login'),

    
    path('logout/', views.logout_view, name='logout'),

    path('register/', views.register, name='register'),
    
     path('index/', views.index, name='index'),

    path('applications/<int:application_id>/', registrar_view, name='registrar_view'),

    path('application/<int:application_id>/update_status/', update_status, name='update_status'),
    
    path('applications/', views.application_list, name='application_list'),  
    path('applications/<int:application_id>/', views.application_detail, name='application_detail'),  
    
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='authentication/password_reset.html',
        form_class=ResetPasswordForm
    ), name='password_reset'),

    
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='authentication/password_reset_done.html'
    ), name='password_reset_done'),

    
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='authentication/password_reset_confirm.html',
        form_class=ResetPasswordConfirmForm
    ), name='password_reset_confirm'),

    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='authentication/password_reset_complete.html'
    ), name='password_reset_complete'),


    path('homepage/',views.homepage, name='homepage'),
    
    
    path('apply/', application_view, name='application_view'), 
    path('apply/success/', TemplateView.as_view(template_name='application/success.html'), name='application_success'),  
    path('track/', track_application, name='track_application')
    
    

]
