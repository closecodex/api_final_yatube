from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router = DefaultRouter()
router.register(prefix='posts', viewset=PostViewSet)
router.register(prefix='groups', viewset=GroupViewSet)
router.register(prefix='follow', viewset=FollowViewSet)
router.register(prefix=r'posts/(?P<post_id>\d+)/comments',
                viewset=CommentViewSet, basename='comments',)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
