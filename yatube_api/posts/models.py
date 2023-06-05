from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Таблица для групп постов."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    """Таблица для хранения постов(Автор и группа поста)."""
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts')
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True, null=True)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Таблица для комментариев к посту."""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments')
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    """Таблица подписок на авторов постов."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )

    class Meta:
        """Ограничение в базе данных поля name."""
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_follows'
            )
        ]

    def __str__(self):
        return f'{self.user} подписался на {self.following}'
