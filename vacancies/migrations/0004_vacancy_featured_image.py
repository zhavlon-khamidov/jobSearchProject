# Generated by Django 4.1.5 on 2023-03-14 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0003_tag_vacancy_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]