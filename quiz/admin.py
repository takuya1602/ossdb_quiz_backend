from django.contrib import admin

from .models import (
    Grade,
    Category,
    SubCategory,
    Question,
    Choice,
)


class ChoiceInline(admin.TabularInline):
    model = Choice


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


admin.site.register(Grade)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Question, QuestionAdmin)
