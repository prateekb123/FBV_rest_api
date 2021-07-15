from django.db import models
from rest_framework import serializers

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    discount = models.IntegerField()
    duration = models.IntegerField()
    author_name = models.CharField(max_length=30)


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'