# Generated by Django 3.0.4 on 2020-03-15 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rest_api', '0009_auto_20200315_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stateoflearningset',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='learning_sets_states', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='stateofverbrektion',
            name='state_of_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.StateOfLearningSet'),
        ),
    ]