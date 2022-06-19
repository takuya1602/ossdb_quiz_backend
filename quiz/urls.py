from django.urls import path

from .views import (
    CategoryList,
    SubCategoryList,
    QuestionDetail,
)

urlpatterns = [
    path("categories/", CategoryList.as_view()),
    path("sub-categories/", SubCategoryList.as_view()),
    path("questions/<int:pk>/", QuestionDetail.as_view()),
]
