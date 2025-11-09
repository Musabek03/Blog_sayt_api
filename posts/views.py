from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post,Category,Tag
from .serializers import PostSerializer,CategorySerializer, TagSerializer
from rest_framework import status


class PostListView(APIView):
    description = "Retrieve a list of blog posts"
    
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            

            
    
    
class PostDetailView(APIView):
    def get(self, request, post_id, format=None):
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self, request, post_id, format=None):
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, post_id, format=None):
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id, format=None):
        post = Post.objects.get(id=post_id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class CategoryListView(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class CategoryDetailView(APIView):
    def get(self, request, category_id, format=None):
        category = Category.objects.get(id=category_id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    def put(self, request, category_id, format=None):
        category = Category.objects.get(id=category_id)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, category_id, format=None):
        category = Category.objects.get(id=category_id)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_id, format=None):
        category = Category.objects.get(id=category_id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class TagListView(APIView):
    def get(self, request, format=None):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class TagDetailView(APIView):
    def get(self,request,tag_id,format=None):
        tag = Tag.objects.get(id = tag_id)
        serializer = TagSerializer(tag)
        return Response(serializer.data)
    
    def put(self, request, tag_id, format=None):
        tag = Tag.objects.get(id = tag_id)
        serializer = TagSerializer(tag, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, tag_id,format=None):
        tag = Tag.objects.get(id = tag_id)
        serializer = TagSerializer(tag, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, tag_id, format=None):
        tag = Tag.objects.get(id = tag_id)
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
