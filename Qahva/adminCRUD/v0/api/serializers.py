from rest_framework import serializers
from ...models import Category

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




