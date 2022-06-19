from django.db import models


class Grade(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    parent_category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Question(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.PROTECT)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    number = models.IntegerField()
    title = models.TextField()
    image = models.ImageField(upload_to="question_images/", null=True, blank=True)
    commentary = models.TextField()

    def __str__(self):
        return self.title


class Choice(models.Model):
    content = models.TextField()
    is_answer = models.BooleanField()
    parent_question = models.ForeignKey(Question, on_delete=models.CASCADE)
