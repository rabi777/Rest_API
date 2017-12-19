from django.shortcuts import render
from django.views.generic import View
import json
from web.models import Student
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from web.serializers import studentSerializer
from rest_framework import generics


class webApiView(APIView):

    def get(self, request):
        student = Student.objects.all()
        serializer = studentSerializer(student, many=True)
        return Response(serializer.data)

class RestApi(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = studentSerializer

