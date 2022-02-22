# Generated by Django 4.0.1 on 2022-02-22 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bilgilerim', '0014_about_job_alter_projects_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Educations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(blank=True, max_length=50)),
                ('department', models.CharField(blank=True, max_length=50)),
                ('startyear', models.CharField(max_length=10)),
                ('finishyear', models.CharField(max_length=10)),
                ('educated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bilgilerim.about')),
            ],
        ),
    ]