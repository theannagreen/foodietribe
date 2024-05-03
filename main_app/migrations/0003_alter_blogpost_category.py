# Generated by Django 4.2.11 on 2024-05-03 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_blogpost_cooking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(blank=True, choices=[('vegan', 'Vegan'), ('vegetarian', 'Vegetarian'), ('pescatarian', 'Pescatarian'), ('halal', 'Halal'), ('kosher', 'Kosher'), ('sugarfree', 'Sugar Free'), ('glutenfree', 'Gluten Free'), ('dairyfree', 'Dairy Free')], max_length=15, null=True),
        ),
    ]
