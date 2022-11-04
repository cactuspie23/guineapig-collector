from django.urls import path
from . import views
from django.views.generic import CreateView, UpdateView, DeleteView

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('guineapigs/', views.guineapigs_index, name='guineapigs_index'),
  path('guineapigs/<int:guineapig_id>/', views.guineapigs_detail, name='guineapigs_detail'),
  path('guineapigs/create/', views.GuineapigCreate.as_view(), name='guineapigs_create'),
]