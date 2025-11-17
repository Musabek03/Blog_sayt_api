from rest_framework import serializers
from .models import Post, Category,Tag,Comment
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

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), 
        source='author', 
        write_only=True
    )

    post_id = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(),
        source='post',
        write_only=True
    )

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author','author_id', 'text', 'post_id', 'created_at']




class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    # author_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='author', write_only=True)
  
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)

    tag = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), source='tag', write_only=True, many=True)

    comments = CommentSerializer(many=True, read_only=True)


    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'category', 'category_id', 'tag', 'tag_ids',  'author','author_id', 'comments','created_at']
    

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = self.context.get('request', None)
        view = self.context.get('view', None)

        if request and view and getattr(view, 'action', None) == 'list':
            self.fields.pop('content', None)
            self.fields.pop('comments',None)