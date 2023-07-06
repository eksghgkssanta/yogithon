# Generated by Django 4.2.1 on 2023-07-06 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('school', models.CharField(max_length=15)),
                ('p_name', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='Images/%Y/%m/%d')),
                ('insta_url', models.URLField()),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('like', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=5)),
                ('last_name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email')),
                ('user_id', models.CharField(max_length=30, unique=True)),
                ('user_pw', models.CharField(max_length=12)),
                ('login_method', models.CharField(choices=[('email', 'Email'), ('Github', 'Github')], default='email', max_length=6)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
