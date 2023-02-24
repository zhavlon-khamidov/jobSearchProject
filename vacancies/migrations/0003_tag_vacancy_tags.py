# Generated by Django 4.1.5 on 2023-02-21 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0002_company_vacancy_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='vacancy',
            name='tags',
            field=models.ManyToManyField(to='vacancies.tag'),
        ),
    ]