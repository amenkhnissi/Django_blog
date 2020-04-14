# Generated by Django 3.0.2 on 2020-02-03 22:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.TextField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
