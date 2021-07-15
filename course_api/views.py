from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course, CourseSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def CourseList(request):

    if request.method=='GET':
        courses  = Course.objects.all()
        serialize = CourseSerializer(courses, many = True)
        return Response(serialize.data)

    elif request.method=='POST':
        serialise = CourseSerializer(data = request.data)
        if serialise.is_valid():
            serialise.save()
            return Response(serialise.data)
        else:
            return Response(serialise.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def CourseDetail(request, pk):

    try:
        course = Course.objects.get(pk=pk)

    except DoesNotExist:
        return Response(status = 404)


    if request.method=='GET':
        serialise = CourseSerializer(course)
        return Response(serialise.data)

    elif request.method=='PUT':
        serialise = CourseSerializer(course, data = request.data)
        if serialise.is_valid():
            serialise.save()
            return Response(serialise.data)
        else:
            return Response(serialise.errors)


    elif request.method=='DELETE':
        course.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)




