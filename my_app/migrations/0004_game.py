# Generated by Django 4.2.8 on 2023-12-11 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_alter_profile_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='game',
            fields=[
                ('game_id', models.AutoField(primary_key=True, serialize=False)),
                ('game_name', models.CharField(max_length=255)),
            ],
        ),
    ]
