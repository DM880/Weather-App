from django.db import models
import datetime
from django.utils.timezone import now

# Create your models here.

class City(models.Model):

    city_name = models.CharField(max_length=50)
    searched = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name_plural = "cities"
