# Generated by Django 3.2 on 2021-06-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.CharField(choices=[('Miscellaneous', 'Miscellaneous'), ('Fashion', 'Fashion'), ('Food', 'Food'), ('Lifestyle', 'Lifestyle'), ('Music', 'Music'), ('Sports', 'Sports'), ('Health', 'Health'), ('Education', 'Education'), ('Software', 'Software'), ('Technology', 'Technology'), ('Fitness', 'Fitness'), ('Cryptocurrency', 'Cryptocurrency'), ('Travel', 'Travel'), ('Personality Development', 'Personality Development'), ('Medicine', 'Medicine'), ('shows', 'shows'), ('movies', 'movies')], default='misc', max_length=25),
        ),
    ]
