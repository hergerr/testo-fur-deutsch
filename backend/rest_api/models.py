from django.db import models

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


class Word(models.Model):
    learning_set = models.ForeignKey(
        LearningSet, on_delete=models.CASCADE, null=False, blank=False, default=1)
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


class VerbRektion(models.Model):
    learning_set = models.ForeignKey(
        LearningSet, on_delete=models.CASCADE, null=False, blank=False, default=1)
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

# TODO model for saving progress
