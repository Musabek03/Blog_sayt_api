from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CategoryViewSet, TagViewSet


router = DefaultRouter()
router.register(r'posts',PostViewSet, basename='post')
router.register(r'category',CategoryViewSet, basename='category' )
router.register(r'tag',TagViewSet, basename='tag')

urlpatterns = router.urls
