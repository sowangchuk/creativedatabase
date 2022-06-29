# Generated by Django 3.2.13 on 2022-06-11 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('heriage', '0002_arts_craft_post_autharts'),
    ]

    operations = [
        migrations.CreateModel(
            name='festival_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discription', models.TextField(max_length=200)),
                ('festival_title', models.CharField(max_length=100)),
                ('festival_image', models.ImageField(upload_to='heriage/festival')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='authfestival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.IntegerField(default=1)),
                ('phone_no', models.IntegerField(unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date_joined')),
                ('document', models.FileField(null=True, upload_to='documents/festival')),
                ('remarks', models.TextField(blank=True, max_length=300)),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
