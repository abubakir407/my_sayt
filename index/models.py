from django.db import models
from django.conf import settings

# Create your models here.
class NewsCategory(models.Model):
        name = models.CharField(max_length=64)
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return str(self.name)



class News(models.Model):
        title = models.CharField(max_length=255)
        content = models.TextField()
        category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now_add=True)
        # favorites = models.ManyToManyField(settings.AUTH_USER_MODEL,
        #                                    related_name='favorite_news',
        #                                    blank=True)

        def __str__(self):
            return str(self.title)

