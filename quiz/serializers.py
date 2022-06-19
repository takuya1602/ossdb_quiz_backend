from rest_framework import serializers

from .models import (
    Category,
    SubCategory,
    Choice,
    Question,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "name",
            "slug",
        )


class SubCategorySerializer(serializers.ModelSerializer):
    parent_category = serializers.StringRelatedField()

    class Meta:
        model = SubCategory
        fields = (
            "name",
            "parent_category",
        )


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = (
            "id",
            "content",
            "is_answer",
        )


class QuestionSerializer(serializers.Serializer):
    grade = serializers.CharField()
    sub_category = serializers.CharField()
    number = serializers.IntegerField()
    title = serializers.CharField()
    image = serializers.ImageField(required=False)
    choice = serializers.ListField(child=ChoiceSerializer())
    # choice = serializers.DictField(child=serializers.BooleanField())
    commentary = serializers.CharField()
