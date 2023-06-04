from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from api.permissions import IsAuthorOrReadOnly
from api.serializers import CommentsSerializer, GroupSerializer, PostSerializer
from posts.models import Group, Post


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(ModelViewSet):
    """Доступ: Аутентификация. Автор редактирует или только чтение."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentsViewSet(ModelViewSet):
    """Доступ к комментариям: Аутентификация."""
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        """Переопределяем метод представления get_queryset."""
        post = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        return post.comments.all()

    def perform_create(self, serializer):
        """Cоздание комментария к посту."""
        post = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        serializer.save(author=self.request.user, post=post)


class CommentsViewSet(ModelViewSet):
    """Доступ: Аутентификация."""
    pass