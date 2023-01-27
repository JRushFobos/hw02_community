from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField(verbose_name="Text")
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    group = models.ForeignKey(
        'Group',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts',
    )

    class Meta:
        ordering = ('-pub_date',)


class Group(models.Model):
    title = models.CharField(max_length=200, help_text='200 characters max.')
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        '''Возвращает строковое представление модели'''
        return self.title
