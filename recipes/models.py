from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    picture = models.URLField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    calories = models.BigIntegerField(null=True)
    have_made = models.BooleanField(default=False)
