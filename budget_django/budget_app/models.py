from django.db import models

# Create your models here.



class Budget(models.Model):
    category = models.CharField(max_length=100)
    amount = models.IntegerField()

    def __str__(self):
        return self.category



