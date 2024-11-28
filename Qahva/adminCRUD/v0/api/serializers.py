from rest_framework import serializers
from ...models import Category, User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id', 'name_ru', 'name_uz', 'slug', 'description_ru', 'description_uz',
            'category_icon', 'is_active', 'created_date', 'modified_date'
        ]


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name_ru', 'name_uz', 'slug', 'description_ru', 'description_uz',
            'category_icon', 'is_active', 'created_date', 'modified_date'
        ]

class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name_ru', 'name_uz', 'slug', 'description_ru', 'description_uz',
            'category_icon', 'is_active'
        ]



class UserCreateSerializer(serializers.ModelSerializer):
    passwordConfirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'passwordConfirm', 'image']

    def validate(self, data):
        if data['password'] != data['passwordConfirm']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        validated_data.pop('passwordConfirm')
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])  # Хэширование пароля
        user.save()
        return user






class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'image', 'createdAt', 'updatedAt']


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'image', 'createdAt', 'updatedAt']


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'image']




