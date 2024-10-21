# Generated by Django 5.1.1 on 2024-10-12 16:37

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_activitylog_id_alter_contactmodel_id'),
        ('inbox', '0002_auto_20241012_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='contact_message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.contactmodel'),
        ),

        migrations.AlterField(
            model_name='conversation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='conversationmessage',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
