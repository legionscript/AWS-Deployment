# Generated by Django 4.1.3 on 2022-12-31 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_published_article_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
