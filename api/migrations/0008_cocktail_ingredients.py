# Generated by Django 4.2.20 on 2025-03-29 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_ingredient_categorization'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='ingredients',
            field=models.ManyToManyField(to='api.ingredient'),
        ),
    ]
