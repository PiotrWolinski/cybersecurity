# Generated by Django 3.1.7 on 2021-05-24 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0003_auto_20210524_1904'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'permissions': [('can_enter_admin_panel', 'Can enter admin panel')]},
        ),
    ]
