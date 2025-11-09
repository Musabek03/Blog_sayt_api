from django.urls import path
from .views import PostListView, PostDetailView,CategoryListView,CategoryDetailView,TagDetailView,TagListView



urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:post_id>/', PostDetailView.as_view(), name='post-detail'),
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('category/<int:category_id>/',CategoryDetailView.as_view(), name='categorydetail-list'),
    path('tag/', TagListView.as_view(),name='tag-list'),
    path('tag/<int:tag_id>/',TagDetailView.as_view(),name='tagdetail-list')


]