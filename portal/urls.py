from django.urls import path
from portal import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('autor_add/', views.autor_add, name='autor_add'),
    path('autor/', views.autor, name='autor'),
    
    path('editora/', views.editora, name='editora'),
    path('formato/', views.formato, name='formato'),
    path('livro/', views.livro, name='livro')
]