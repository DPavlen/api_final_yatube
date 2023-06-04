from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentsViewSet, FollowViewSet, GroupViewSet, PostViewSet


router_v1 = DefaultRouter()
router_v1.register("posts", PostViewSet, basename="posts")
router_v1.register("groups", GroupViewSet, basename="groups")
router_v1.register("follows", FollowViewSet, basename="follows")
router_v1.register(
    r"posts/(?P<post_id>\d+)/comments",
    CommentsViewSet, basename="comments"
)

urlpatterns = [
    path("v1/", include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
