# Generated by Django 4.1 on 2023-04-22 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Q_app', '0003_rename_client_id_requirements_clientid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requirements',
            old_name='clientid',
            new_name='deptid',
        ),
    ]
