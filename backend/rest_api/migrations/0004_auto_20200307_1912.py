# Generated by Django 3.0.4 on 2020-03-07 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0003_auto_20200304_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='LearningSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('last_success_rate', models.IntegerField(default=0)),
                ('type_of_set', models.CharField(choices=[('verb_rektion', 'Verb Rektion'), ('vocabulary', 'Wortshatz')], max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='verbrektion',
            name='verbs_rektion_set',
        ),
        migrations.RemoveField(
            model_name='word',
            name='word_set',
        ),
        migrations.DeleteModel(
            name='VerbsRektionSet',
        ),
        migrations.DeleteModel(
            name='WordSet',
        ),
        migrations.AddField(
            model_name='verbrektion',
            name='learning_set',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rest_api.LearningSet'),
        ),
        migrations.AddField(
            model_name='word',
            name='learning_set',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rest_api.LearningSet'),
        ),
    ]
