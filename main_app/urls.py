from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('guineapigs/', views.guineapigs_index, name='guineapigs_index'),
  path('guineapigs/<int:guineapig_id>/', views.guineapigs_detail, name='guineapigs_detail'),
]