# Generated by Django 2.2.4 on 2019-08-20 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('verified_student', models.BooleanField(default=False)),
                ('college', models.CharField(blank=True, max_length=80)),
                ('college_email', models.EmailField(blank=True, max_length=254)),
                ('grad_date', models.DateField(blank=True, null=True)),
                ('discord', models.CharField(blank=True, max_length=32)),
                ('faceit', models.CharField(blank=True, max_length=32)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
