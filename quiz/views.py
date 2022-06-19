from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import (
    Category,
    SubCategory,
    Question,
    Choice,
)

from .serializers import (
    CategorySerializer,
    SubCategorySerializer,
    QuestionSerializer,
)


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryList(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class QuestionList(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        questions = Question.objects.filter(
            sub_category__parent_category__slug=request.query_params.get(
                "category-name"
            )
        )
        return questions


class QuestionDetail(APIView):
    def get(self, request, pk, *args, **kwargs):
        question = Question.objects.select_related("grade", "sub_category").get(pk=pk)
        choices = Choice.objects.filter(parent_question=pk)

        choice_data = dict()
        for choice in choices:
            choice_data[choice.content] = choice.is_answer

        question_data = {
            "grade": question.grade.name,
            "sub_category": question.sub_category.name,
            "number": question.number,
            "title": question.title,
            "image": question.image,
            "choice": choices,
            "commentary": question.commentary,
        }

        # if "image" is None, Response(question_data) raise error.
        # so, use QuestionSerializer in which
        # ...
        # image = serializers.ImageField(required=False)
        # ...
        serializer = QuestionSerializer(question_data)

        return Response(serializer.data)
