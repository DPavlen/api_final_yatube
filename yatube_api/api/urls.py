from django.urls import include, path
# from rest_framework import routers

# from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
]