from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True)  # idle, waiting, playing

    def __str__(self):
        return self.name


class MatchStatus(models.Model):
    in_progress = models.BooleanField(default=False)
    goals_player1 = models.IntegerField(default=0)
    goals_player2 = models.IntegerField(default=0)
    has_player1_yellow_card = models.BooleanField(default=False)
    has_player2_yellow_card = models.BooleanField(default=False)
    red_cards_player1 = models.IntegerField(default=0)
    red_cards_player2 = models.IntegerField(default=0)


class Match(models.Model):
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='matches_as_player1', null=True)
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='matches_as_player2', null=True)
    status = models.ForeignKey(MatchStatus, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.player1.name + ' vs. ' + self.player2.name


class Round(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    in_progress = models.BooleanField(default=False)
    letters_player1 = models.IntegerField(default=0)
    letters_player2 = models.IntegerField(default=0)


class Word(models.Model):
    round = models.ForeignKey(Round, on_delete=models.CASCADE, null=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=200, null=True)
    is_in_dict = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.text


