from django.urls import path, include
from rest_framework import routers
from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'posts/(?P<post_id>[^/.]+)/comments',
                CommentViewSet, basename='comments')
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.jwt')),
]
