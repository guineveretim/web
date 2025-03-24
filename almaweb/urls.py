from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('journals/', views.Journal, name= 'journals'),
       path('download/<int:article_id>/', views.download_article, name='download_article'),
    path('consultancy_unit/', views.Consultancy, name= 'consulting'),
    path('payments/', views.Payment, name= 'payments'),
    path('about/', views.About, name= 'about'),
    path('agri-business/', views.Agribusiness, name= 'agribusiness'),
    path('mba/', views.MBA, name= 'mba'),
    path('clm/', views.CLM, name= 'clm'),
    path('ilf/', views.ILF, name= 'ilf'),
    path('btlgs/', views.BTLGS, name= 'btlgs'),
]
