# Generated by Django 3.2 on 2021-04-24 17:27

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_tag', models.CharField(max_length=255)),
                ('header_image', models.ImageField(upload_to='images/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('body', ckeditor.fields.RichTextField()),
                ('category', models.CharField(default='coding', max_length=255)),
                ('snippet', models.CharField(max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]