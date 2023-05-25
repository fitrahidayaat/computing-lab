from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    publisher = models.CharField(max_length=250)
    abstract = models.TextField(max_length=10000)
    year = models.CharField(max_length=4)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Publications'