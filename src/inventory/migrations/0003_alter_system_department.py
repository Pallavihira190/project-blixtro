# Generated by Django 4.2 on 2025-03-02 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('inventory', '0002_alter_room_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.department'),
        ),
    ]
