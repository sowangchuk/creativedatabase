# Generated by Django 4.0.5 on 2022-06-19 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('functional_creation', '0006_graphic_post_auth_graphic_auth_architecture_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='auth_advertising',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.IntegerField(default=1)),
                ('phone_no', models.IntegerField(unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date_joined')),
                ('document', models.FileField(null=True, upload_to='documents/cre/fun/ad')),
                ('remarks', models.TextField(blank=True, max_length=300)),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='advertising_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discription', models.TextField(max_length=200)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='function/ad')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
