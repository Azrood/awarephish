# Generated by Django 3.0.5 on 2020-05-11 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_auto_20200510_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reponses',
            name='correct_answer',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Réponses correctes'),
        ),
        migrations.AlterField(
            model_name='reponses',
            name='wrong_answers',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Réponses Incorrectes'),
        ),
    ]
