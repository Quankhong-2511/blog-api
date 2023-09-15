from django.shortcuts import render
from .models import CustomUser, Blog
from .serializers import CustomUserSerializer, BlogSerializer, DetailSerializer
from rest_framework.response import Response
from rest_framework import views, status, generics



class CustomUserAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class BlogAPIView(views.APIView):
    def get(self, request):
        data = Blog.objects.all()
        serializer = BlogSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 



class DetaiAPIView(generics.RetrieveAPIView,
                   generics.CreateAPIView,
                   generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = DetailSerializer

