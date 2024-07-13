from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255,default='title')
    summary = models.TextField()
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
