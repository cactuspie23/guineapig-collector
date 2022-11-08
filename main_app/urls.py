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
  path('guineapigs/<int:guineapig_id>/assoc_accessory/<int:accessory_id>/', views.assoc_accessory, name='assoc_accessory'),
  path('accessories/create/', views.AccessoryCreate.as_view(), name='accessories_create'),
  path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name='accessories_detail'),
  path('accessories/', views.AccessoryList.as_view(), name='accessories_index'),
  path('accessories/<int:pk>/update/', views.AccessoryUpdate.as_view(), name='accessories_update'),
  path('accessories/<int:pk>/delete/', views.AccessoryDelete.as_view(), name='accessories_delete'),
]
