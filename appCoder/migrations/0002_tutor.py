# Generated by Django 4.1.6 on 2023-02-17 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('mail', models.EmailField(max_length=254)),
                ('Profesion', models.CharField(max_length=20)),
            ],
        ),
    ]
