# Generated by Django 4.2 on 2025-02-20 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_userprofile_is_institution_admin_and_more'),
        ('inventory', '0017_purchase_added_to_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt', models.FileField(upload_to='receipts/')),
                ('remarks', models.TextField()),
                ('completed_on', models.DateTimeField(auto_now_add=True)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.organisation')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipt', to='inventory.purchase')),
            ],
        ),
        migrations.DeleteModel(
            name='PurchaseCompletion',
        ),
    ]
