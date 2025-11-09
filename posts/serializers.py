from rest_framework import serializers
from .models import Post, Category,Tag
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']




class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='author', write_only=True)
  
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)

    tag = TagSerializer(many=True, read_only=True)
    tag_id = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), source='tag', write_only=True, many=True)


    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'category', 'category_id', 'tag', 'tag_id',  'author','author_id',  'created_at']
