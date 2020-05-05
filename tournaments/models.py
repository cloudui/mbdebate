from django.db import models


from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse 

class Tournament(models.Model):
    name = models.CharField(max_length=255)
    date = models.CharField(max_length=10)
    cost = models.CharField(max_length=10)
    link = models.CharField(max_length=50, null=True)
    
    slug = models.SlugField(null=False, unique=True, default=None)

    # date = models.DateTimeField(auto_now_add=True)

    # author = models.ForeignKey(
    #     get_user_model(),
    #     on_delete=models.CASCADE,
    # )

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('article_detail', args=[str(self.id)])

