# Generated by Django 5.0.4 on 2024-04-30 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='',
            field=models.CharField(choices=[('vegan', 'Vegan'), ('vegetarian', 'Vegetarian'), ('pescatarian', 'Pescatarian'), ('halal', 'Halal'), ('kosher', 'Kosher'), ('sugarfree', 'Sugar Free'), ('glutenfree', 'Gluten Free'), ('dairyfree', 'Dairy Free')], max_length=50),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('blogpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.blogpost')),
            ],
        ),
    ]
