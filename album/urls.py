from django.urls import path, include
from album import views

urlpatterns = [
    path('', views.base, name='base'),
    path('category', views.category, name='category-list'),
    path('category/detail<int:category_id>/', views.category_detail, name='category-detail'),
    path('category/update<int:pk>/', views.CategoryUpdate.as_view(), name='category-update'),
    path('category/create', views.CategoryCreate.as_view(), name='category-create'),
    path('category/delete<int:pk>/', views.CategoryDelete.as_view(), name='category-delete'),

    path('photo', views.PhotoListView.as_view(), name='photo-list'),
    
    path('photo/detail<int:pk>/', views.PhotoDetailView.as_view(), name='photo-detail'),
    path('photo/update<int:pk>/', views.PhotoUpdate.as_view(), name='photo-update'),
    path('photo/create', views.PhotoCreate.as_view(), name='photo-create'),
    path('photo/delete<int:pk>/', views.PhotoDelete.as_view(), name='photo-delete'),
]