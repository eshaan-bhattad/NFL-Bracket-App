# Generated by Django 2.1.15 on 2021-01-13 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bracket',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('afcWildCard1', models.CharField(max_length=200)),
                ('afcWildCard2', models.CharField(max_length=200)),
                ('afcWildCard3', models.CharField(max_length=200)),
                ('nfcWildCard1', models.CharField(max_length=200)),
                ('nfcWildCard2', models.CharField(max_length=200)),
                ('nfcWildCard3', models.CharField(max_length=200)),
                ('afcDivisional1', models.CharField(max_length=200)),
                ('afcDivisional2', models.CharField(max_length=200)),
                ('nfcDivisional1', models.CharField(max_length=200)),
                ('nfcDivisional2', models.CharField(max_length=200)),
                ('afcChampions', models.CharField(max_length=200)),
                ('nfcChampions', models.CharField(max_length=200)),
                ('superbowl', models.CharField(max_length=200)),
                ('superbowlTieBreaker', models.IntegerField()),
                ('points', models.IntegerField()),
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]