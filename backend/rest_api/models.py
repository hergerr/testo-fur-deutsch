from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class LearningSet(models.Model):
    date_created = models.DateField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    last_success_rate = models.IntegerField(
        default=0)  # success rate in percents
    type_of_set = models.CharField(
        max_length=30,
        choices=[
            ('verb_rektion', 'Verb Rektion'),
            ('vocabulary', 'Wortshatz')
        ]
    )

    def __str__(self):
        return f"{self.title} Wortschatz"


class StateOfLearningSet(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False)
    learning_set = models.ForeignKey(
        LearningSet, on_delete=models.CASCADE, null=False, blank=False
    )
    number_of_obligaory_rounds = models.IntegerField(default=1)
    percent_done = models.IntegerField(default=0)
    corectness_rate = models.IntegerField(default=0)


class Word(models.Model):
    learning_set = models.ForeignKey(
        LearningSet, on_delete=models.CASCADE, null=False, blank=False)
    german_word = models.CharField(max_length=100)
    article = models.CharField(
        max_length=3,
        null=True,
        blank=True,
        choices=[
            ('der', 'der'),
            ('die', 'die'),
            ('das', 'das')
        ]
    )
    translation = models.CharField(max_length=100)
    part_of_speech = models.CharField(
        max_length=30,
        choices=[
            ('verb', 'das Verb'),
            ('noun', 'das Substantiv'),
            ('adjective', 'das Adjektiv'),
            ('conjunction', 'die Konjunktion'),
            ('other', 'andere')
        ]
    )

    def __str__(self):
        return f"{self.german_word}"


class StateOfWord(models.Model):
    state_of_set = models.ForeignKey(
        StateOfLearningSet, on_delete=models.CASCADE, null=False, blank=False)
    word = models.ForeignKey(
        Word, on_delete=models.CASCADE, null=False, blank=False)
    done = models.BooleanField(default=False)
    number_of_correct_answers = models.IntegerField(default=0)


class VerbRektion(models.Model):
    learning_set = models.ForeignKey(
        LearningSet, on_delete=models.CASCADE, null=False, blank=False)
    phrase = models.TextField()
    case = models.CharField(
        max_length=1,
        choices=[
            ('n', 'Nominativ'),
            ('g', 'Genitiv'),
            ('d', 'Dativ'),
            ('a', 'Akkusativ')
        ]
    )
    translation = models.TextField()
    example = models.TextField()

    def __str__(self):
        return f"{self.phrase}"


class StateOfVerbRektion(models.Model):
    state_of_set = models.ForeignKey(
        StateOfLearningSet, on_delete=models.CASCADE, null=False, blank=False)
    verb_rektion = models.ForeignKey(
        VerbRektion, on_delete=models.CASCADE, null=False, blank=False)
    done = models.BooleanField(default=False)
    number_of_correct_answers = models.IntegerField(default=0)
