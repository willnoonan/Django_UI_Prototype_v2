from django.db import models

# Create your models here.
from configurations.models import Configuration


class Project(models.Model):
    configuration = models.ForeignKey(Configuration, on_delete=models.PROTECT)
    #TODO: The other possible values for on_delete are: CASCADE (don't want this one), RESTRICT (not sure about this one)
    name = models.CharField(max_length=200)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'projects'

    def __str__(self):
        text = self.name
        size = 50
        string = f'{text[:size]}'
        return string if len(string) < size else string + '...'