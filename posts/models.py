from datetime import date, datetime
from email import contentmanager
from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
from groups.models import Group

User = get_user_model()
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, related_name = "posts", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now = True)
    message = models.TextField()
    group = models.ForeignKey(Group, on_delete = models.CASCADE, related_name = "posts")
    class Meta:
        ordering = ['-created_at', 'group']
    def __str__(self):
        return self.message
    