# Generated by Django 4.1.7 on 2023-04-26 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_articles_options_alter_sentences_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='content',
            field=models.TextField(),
        ),
    ]