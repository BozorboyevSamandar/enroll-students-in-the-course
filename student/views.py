from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CourseSerializer, StudentSerializer
from .models import Course, Student


# Create your views here.


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
