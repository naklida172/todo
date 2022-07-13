from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

user = get_user_model()

class Task(models.Model):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='tasks'
                              )
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        
    # TODO: добавить ордеринг
    def __str__(self):
        return self.title
