from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from ...models import Category
from .serializers import CategorySerializer, CategoryDetailSerializer, CategoryUpdateSerializer
from django.utils import timezone
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, get_object_or_404, UpdateAPIView
from rest_framework.permissions import IsAdminUser


class CategoryCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        try:
            category = Category.objects.get(id=pk)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategoryDetailSerializer(category)
        response_data = {
            "status": "OK",
            "serverTime": int(timezone.now().timestamp()),
            "category": serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)



class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


class CategoryDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAdminUser]
    model = Category

    def delete(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        self.check_object_permissions(self.request, category)
        self.perform_destroy(category)
        response_data = {
            "status": "OK",
            "serverTime": int(timezone.now().timestamp()),
            'message': 'Category deleted successfully.'
        }
        return Response(response_data)


class CategoryUpdateAPIView(UpdateAPIView):
    serializer_class = CategoryUpdateSerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]
    def get_object(self):
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj
