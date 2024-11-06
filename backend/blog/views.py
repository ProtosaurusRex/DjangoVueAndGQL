from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Post
from rest_framework import generics
from .serializers import PostSerializer

class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

