from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
TEXT = 25


class Group(models.Model):
    """Модель групп."""

    title = models.CharField('Группа', max_length=200)
    slug = models.SlugField('slug', unique=True)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title[:TEXT]

    class Meta:
        ordering = ('title',)


class Post(models.Model):
    """Модель постов."""

    text = models.TextField('text')
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
        verbose_name='Изображение'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
        verbose_name='Группа'
    )

    def __str__(self):
        return self.text[:TEXT]

    class Meta:
        ordering = ['pub_date']


class Comment(models.Model):
    """"Модель комментариев."""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='comments'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Пост',
        related_name='comments'
    )
    text = models.TextField('Текст')
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )

    def __str__(self):
        return self.text[:TEXT]


class Follow(models.Model):
    """"Модель подписки на автора."""

    user = models.ForeignKey(
        User,
        verbose_name='Подписчик',
        on_delete=models.CASCADE,
        related_name='follower',
    )
    following = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='following',
    )

    def __str__(self):
        return f'{self.user} подписчик автора - {self.following}'

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=~models.Q(user=models.F('following')),
                name='%(app_label)s_%(class)s_prevent_self_follow'
            )
        ]
