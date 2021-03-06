# Generated by Django 4.0.1 on 2022-02-13 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_setting_aboutus_setting_aboutme'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=100)),
                ('subject', models.CharField(blank=True, max_length=100)),
                ('message', models.CharField(blank=True, max_length=200)),
                ('status', models.CharField(choices=[('New', 'Yeni'), ('Read', 'Okundu')], default='New', max_length=10)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('note', models.CharField(blank=True, max_length=100)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
