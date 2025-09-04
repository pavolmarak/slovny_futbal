from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Word(models.Model):
    text = models.CharField(max_length=200)
    player_id = models.IntegerField(default=0)
    is_in_dict = models.BooleanField(default=False)

    def __str__(self):
        return self.text