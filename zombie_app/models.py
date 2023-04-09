from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Zombie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    strength = models.IntegerField(validators=[MaxValueValidator(10)])
    weakness = models.CharField(max_length=255)
    attack_plan = models.TextField()
    antidote = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.name
    

class ZombieAttack(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=255)
    date = models.DateField()
    zombie = models.OneToOneField('Zombie', on_delete=models.CASCADE, default=None)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.location} ({self.date})'