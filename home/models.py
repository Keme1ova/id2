from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=20)
    img = models.ImageField(upload_to="")
    text = models.TextField()

    def __str__(self):
        return self.title


