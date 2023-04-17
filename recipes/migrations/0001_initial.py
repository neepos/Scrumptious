# Generated by Django 4.2 on 2023-04-17 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('picture', models.URLField()),
                ('description', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('calories', models.BigIntegerField(null=True)),
                ('have_made', models.BooleanField(default=False)),
            ],
        ),
    ]
