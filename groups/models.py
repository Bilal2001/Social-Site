from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
# import misaka

User = get_user_model()

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length = 25, unique = True)
    slug = models.SlugField(allow_unicode = True, unique = True)
    desc = models.TextField(blank = True, default = '')
    desc_html = models.TextField(blank = True, default = '')
    members = models.ManyToManyField(User, through = "GroupMember")
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        # to redirect to list page
        return reverse('groups:list')
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.desc_html = self.desc #misaka.html(self.desc)
        super().save(*args, **kwargs)

class GroupMember(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="membership")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usergroup")
    def __str__(self):
        return self.user.username
    class Meta:
        ordering = ['user']