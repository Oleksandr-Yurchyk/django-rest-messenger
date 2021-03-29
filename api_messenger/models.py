from django.db import models


class Message(models.Model):
    author_email = models.CharField(max_length=36)
    text = models.TextField(max_length=105)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Message id #{self.pk}'
