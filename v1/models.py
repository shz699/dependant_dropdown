from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Countries' 

    def __str__(self) -> str:
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country , on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'Cities' 

    def __str__(self) -> str:
        return self.name    