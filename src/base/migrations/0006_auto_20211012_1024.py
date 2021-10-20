# Generated by Django 3.2.8 on 2021-10-12 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0005_logement_ville'),
    ]

    operations = [
        migrations.AddField(
            model_name='logement',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logement',
            name='ville',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='base.ville'),
            preserve_default=False,
        ),
    ]