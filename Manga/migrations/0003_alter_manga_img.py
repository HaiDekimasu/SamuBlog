# Generated by Django 5.0.1 on 2024-01-19 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manga', '0002_alter_manga_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='img',
            field=models.ImageField(upload_to='img/'),
        ),
    ]