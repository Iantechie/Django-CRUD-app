from django.db import models

# Create your models here.
class Members(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)

    def __str__(self):
        return self.name
    