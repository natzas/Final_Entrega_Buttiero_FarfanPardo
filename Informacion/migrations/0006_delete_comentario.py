# Generated by Django 4.0.4 on 2022-07-01 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Informacion', '0005_comentario_avatar'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comentario',
        ),
    ]