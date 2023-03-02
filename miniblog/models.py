from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=70)
    des = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']