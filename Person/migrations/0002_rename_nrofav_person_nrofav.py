# Generated by Django 4.1.2 on 2022-10-12 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='Nrofav',
            new_name='nrofav',
        ),
    ]
