# Generated by Django 3.2.8 on 2021-10-10 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lib', models.CharField(db_column='libNiv', max_length=200)),
                ('createdAt', models.DateTimeField(auto_now_add=True, db_column='niv_createdAt')),
                ('updatedAt', models.DateTimeField(auto_now=True, db_column='niv_updatedAt')),
            ],
        ),
    ]
