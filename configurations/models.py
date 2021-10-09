from django.db import models

# Create your models here.

class Configuration(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    #TODO add properties

    def __str__(self):
        return self.name