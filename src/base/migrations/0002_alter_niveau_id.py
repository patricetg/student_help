# Generated by Django 3.2.8 on 2021-10-10 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='niveau',
            name='id',
            field=models.AutoField(db_column='idNiv', primary_key=True, serialize=False),
        ),
    ]
