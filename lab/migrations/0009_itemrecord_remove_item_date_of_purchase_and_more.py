# Generated by Django 4.2 on 2024-07-30 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0008_alter_systemcomponent_component_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('remarks', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='date_of_purchase',
        ),
        migrations.DeleteModel(
            name='LabRecord',
        ),
        migrations.AddField(
            model_name='itemrecord',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.item'),
        ),
        migrations.AddField(
            model_name='itemrecord',
            name='lab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.lab'),
        ),
    ]
