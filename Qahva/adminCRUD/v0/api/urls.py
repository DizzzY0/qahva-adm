
from django.urls import path
from .views import (
    CategoryCreateView, 
    CategoryDetailView, 
    CategoryListAPIView, 
    CategoryDeleteAPIView, 
    CategoryUpdateAPIView,
    #
    UserCreateAPIView,
    UserDetailAPIView,
    UserListAPIView,
    UserProfileImageAPIView,
    UserUpdateAPIView,
)

app_name = 'control_api'

urlpatterns = [
    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
    path('category/details/<pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('category/list/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/delete/<pk>', CategoryDeleteAPIView.as_view(), name = 'category-delete'),
    path('category/update/<pk>', CategoryUpdateAPIView.as_view(), name='category-update'),

    # 

    path('users', UserCreateAPIView.as_view(), name='user-create'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('users/all/', UserListAPIView.as_view(), name='user-list'),
    path('users/images/', UserProfileImageAPIView.as_view(), name='user-image'),
    path('users/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
]
