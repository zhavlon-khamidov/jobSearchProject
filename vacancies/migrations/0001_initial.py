# Generated by Django 4.1.5 on 2023-02-17 09:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('min_price', models.IntegerField(default=0)),
                ('max_price', models.IntegerField(default=0)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
