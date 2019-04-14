from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

from django.db import models


class User(models.Model):
    sexes = (
        ('male', "男"),
        ('female', '女'),
    )
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=50, choices=sexes, default='? ')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-c_time', 'name']
        verbose_name = 'user'