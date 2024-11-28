from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, get_object_or_404, UpdateAPIView, RetrieveAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from ...models import Category
from ...models import User
from .serializers import (
    CategorySerializer, 
    CategoryDetailSerializer, 
    CategoryUpdateSerializer,
    #
    UserCreateSerializer,
    UserDetailSerializer,
    UserListSerializer,
    UserUpdateSerializer,
)
from django.utils import timezone



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

# class CategoryDeleteAPIView(DestroyAPIView):
#     permission_classes = [IsAdminUser]
#     model = Category

#     def delete(self, request, pk):
#         category = get_object_or_404(Category, id=pk)
#         self.check_object_permissions(self.request, category)
#         self.perform_destroy(category)
#         response_data = {
#             "status": "OK",
#             "serverTime": int(timezone.now().timestamp()),
#             'message': 'Category deleted successfully.'
#         }
#         return Response(response_data)

class CategoryDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()  # Добавьте этот атрибут для корректной работы
    serializer_class = None  # Если сериализатор не нужен для удаления

    def delete(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        self.check_object_permissions(self.request, category)
        self.perform_destroy(category)
        response_data = {
            "status": "OK",
            "serverTime": int(timezone.now().timestamp()),
            "message": "Category deleted successfully.",
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

###



# class UserCreateAPIView(CreateAPIView):
#     serializer_class = UserCreateSerializer
#     parser_classes = [MultiPartParser, FormParser]

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response(
#             {
#                 "status": "OK",
#                 "user": serializer.data,
#             },
#             status=status.HTTP_201_CREATED,
#         )

#     # Добавляем get_queryset для предотвращения ошибок в Swagger
#     def get_queryset(self):
#         return User.objects.none()  # Возвращает пустой QuerySet



class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]   

    def get_queryset(self):
        # Возвращаем пустой QuerySet, чтобы избежать ошибок
        return User.objects.none()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        response_data = {
            "status": "OK",
            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "image": user.image.url if user.image else None,
                "createdAt": user.createdAt.strftime('%Y-%m-%d %H:%M:%S'),
                "updatedAt": user.updatedAt.strftime('%Y-%m-%d %H:%M:%S'),
            }
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = "pk"


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserProfileImageAPIView(APIView):
    def get(self, request, *args, **kwargs):
        image_url = request.query_params.get("url")
        if not image_url:
            return Response({"error": "No image URL provided"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            with open(image_url, "rb") as image_file:
                return Response({"image": image_file.read()}, content_type="image/jpeg")
        except FileNotFoundError:
            return Response({"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND)


class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer