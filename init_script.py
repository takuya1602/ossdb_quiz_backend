from quiz.models import (
    SubCategory,
    Question,
    Choice,
)

Choice.objects.all().delete()
Question.objects.all().delete()
SubCategory.objects.all().delete()
