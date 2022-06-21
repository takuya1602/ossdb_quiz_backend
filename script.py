import json

from quiz.models import (
    Grade,
    Category,
    SubCategory,
    Question,
    Choice,
)

with open("scrape/questions.json", "r") as f:
    questions = json.load(f)

# Subcategory
sub_and_parent_categories = dict()
for q in questions:
    category, sub_category = q["category"], q["sub_category"]
    if sub_category not in sub_and_parent_categories.keys():
        sub_and_parent_categories[sub_category] = category

for sub_category, parent_category in sub_and_parent_categories.items():
    parent_category_obj = Category.objects.get(slug=parent_category)
    SubCategory(
        name=sub_category,
        parent_category=parent_category_obj,  # foreign key
    ).save()

# Question and Chocie
for q in questions:
    grade_obj = Grade.objects.get(slug=q["grade"])
    sub_category_obj = SubCategory.objects.get(name=q["sub_category"])
    question_obj = Question(
        grade=grade_obj,  # foreign key
        sub_category=sub_category_obj,  # foreing key
        number=q["number"],
        title=q["title"],
        commentary=q["commentary"],
    )
    question_obj.save()

    for i, choice in enumerate(q["choice"]):
        if chr(65 + i) in q["answer"]:
            is_answer = True
        else:
            is_answer = False
        Choice(
            content=choice,
            is_answer=is_answer,
            parent_question=question_obj,
        ).save()
