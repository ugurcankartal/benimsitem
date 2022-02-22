# Generated by Django 4.0.1 on 2022-02-22 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bilgilerim', '0015_educations'),
    ]

    operations = [
        migrations.CreateModel(
            name='languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, max_length=20)),
                ('lewel', models.CharField(blank=True, max_length=10)),
                ('ownlanguage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bilgilerim.about')),
            ],
        ),
        migrations.CreateModel(
            name='allworks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(blank=True, max_length=20)),
                ('companyname', models.CharField(blank=True, max_length=20)),
                ('companysite', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('startyear', models.CharField(max_length=10)),
                ('finishyear', models.CharField(max_length=10)),
                ('ownwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bilgilerim.about')),
            ],
        ),
    ]