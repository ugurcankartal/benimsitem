# Generated by Django 4.0.1 on 2022-04-09 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bilgilerim', '0019_projects_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimages',
            name='images_name',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
