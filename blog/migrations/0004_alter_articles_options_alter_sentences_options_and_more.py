# Generated by Django 4.1.7 on 2023-04-18 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_articles_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name_plural': 'articles'},
        ),
        migrations.AlterModelOptions(
            name='sentences',
            options={'verbose_name_plural': 'sentences'},
        ),
        migrations.AlterModelOptions(
            name='tags',
            options={'verbose_name_plural': 'tags'},
        ),
        migrations.AlterModelOptions(
            name='words',
            options={'verbose_name_plural': 'words'},
        ),
    ]
