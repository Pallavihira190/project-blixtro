# Generated by Django 4.2 on 2024-05-14 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_userprofile_is_lab_staff'),
        ('lab', '0002_lab_org'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='user',
            field=models.ManyToManyField(to='core.userprofile'),
        ),
    ]
