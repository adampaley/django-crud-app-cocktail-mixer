# Generated by Django 4.2.20 on 2025-03-28 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_cocktail_glassware'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktail',
            name='glassware',
            field=models.CharField(choices=[('C', 'collins'), ('H', 'highball'), ('M', 'martini'), ('R', 'rocks'), ('S', 'shot'), ('U', 'coupe'), ('W', 'wine')], default='H', max_length=1),
        ),
    ]
