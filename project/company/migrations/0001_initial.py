# Generated by Django 5.0.7 on 2024-08-02 05:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0004_remove_post_applicants_post_applicants'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000)),
                ('location', models.CharField(max_length=2000)),
                ('desc', models.CharField(max_length=10000)),
                ('phone_number', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('fb_id', models.CharField(max_length=100)),
                ('ld_id', models.CharField(max_length=100)),
                ('x_id', models.CharField(max_length=100)),
                ('ig_id', models.CharField(max_length=100)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
        ),
    ]
