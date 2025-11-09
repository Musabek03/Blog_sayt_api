from django.urls import path
from .views import PostListView, PostDetailView,CategoryListView,CategoryDetailView,TagDetailView,TagListView



urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('category/<int:pk>/',CategoryDetailView.as_view(), name='categorydetail-list'),
    path('tag/', TagListView.as_view(),name='tag-list'),
    path('tag/<int:pk>/',TagDetailView.as_view(),name='tagdetail-list')


]