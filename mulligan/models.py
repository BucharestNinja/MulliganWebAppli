from django.db import models

# Create your models here.
class Deck(models.Model):
    card=models.TextField()
