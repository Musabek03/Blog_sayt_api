from .models import Post,Category,Tag,Comment,User
from .serializers import PostSerializer,CategorySerializer, TagSerializer,CommentSerializer,UserSerializer
from rest_framework import viewsets,filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly, IsAdminOrReadOnly, IsAdminOrCreateOnlyOrReadOnly
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend


@extend_schema(tags=['Posts'])
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category__name']
    search_fields = ['title', 'content']
    


    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

    def list(self,request, *args, **kwargs):
        response = super().list(request,*args, **kwargs)
        posts_data = response.data.get('results', response.data)

        for post in posts_data:
            content = post.get('content', '')
            if len(content) > 70:
                post['content'] = content[:70] + '...'

        return response


@extend_schema(tags=['Category'])
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = None
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

@extend_schema(tags=['Tags'])
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = None
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

@extend_schema(tags=['Comments'])
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

@extend_schema(tags=['Users'])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']
    permission_classes = [permissions.IsAdminUser]

    
