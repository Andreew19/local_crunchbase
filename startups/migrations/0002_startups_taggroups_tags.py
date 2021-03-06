# Generated by Django 3.2.10 on 2022-03-28 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Startups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('url', models.TextField()),
                ('publicated_at', models.DateTimeField(verbose_name='date published')),
                ('updated_at', models.DateTimeField(verbose_name='date updated')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('name', models.CharField(max_length=256)),
                ('publicated_at', models.DateTimeField(verbose_name='date published')),
                ('updated_at', models.DateTimeField(verbose_name='date updated')),
                ('tag_group_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('startups_tags', models.ManyToManyField(to='startups.Startups')),
            ],
        ),
        migrations.CreateModel(
            name='TagGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('publicated_at', models.DateTimeField(verbose_name='date published')),
                ('updated_at', models.DateTimeField(verbose_name='date updated')),
                ('tag_group_id', models.ManyToManyField(to='startups.Tags')),
            ],
        ),
    ]
