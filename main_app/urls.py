from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('guineapigs/', views.guineapigs_index, name='guineapigs_index'),
  path('guineapigs/<int:guineapig_id>/', views.guineapigs_detail, name='guineapigs_detail'),
  path('guineapigs/create/', views.GuineapigCreate.as_view(), name='guineapigs_create'),
  path('guineapigs/<int:pk>/update/', views.GuineapigUpdate.as_view(), name='guineapig_update'),
  path('guineapigs/<int:pk>/delete/', views.GuineapigDelete.as_view(), name='guineapig_delete'),
  path('guineapigs/<int:guineapig_id>/add_feeding/', views.add_feeding, name='add_feeding'),
]
