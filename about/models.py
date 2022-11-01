from django.db import models

# Create your models here.
class bubuk(models.Model):
    nama = models.CharField(max_length=150)

    def __str__(self):
        return self.nama