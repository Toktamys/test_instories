from django.db import models
from django.urls import reverse
from datetime import datetime


class Option(models.Model):
    name = models.CharField(max_length=255)
    value = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    def get_absolute_url(self):
        return reverse('option_detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('option_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('option_delete', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False) -> None:
        self.is_deleted = True
        self.deleted_at = datetime.now()
        self.save()


class Push(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pushed_at = models.DateTimeField(null=True)
    is_sent = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)

    def get_absolute_url(self):
        return reverse('push_detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('push_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('push_delete', kwargs={'pk': self.pk})

    def __str__(self):
        return '{title} - {date}'.format(
            title=self.title,
            date=self.pushed_at if self.is_sent else ''
        )

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = datetime.now()
        self.save()
