
from django.urls import path
from .views import CategoryCreateView, CategoryDetailView, CategoryListAPIView, CategoryDeleteAPIView, CategoryUpdateAPIView
app_name = 'control_api'

urlpatterns = [
    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
    path('category/details/<pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('category/list/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/delete/<pk>', CategoryDeleteAPIView.as_view(), name = 'category-delete'),
    path('category/update/<pk>', CategoryUpdateAPIView.as_view(), name='category-update')
]
