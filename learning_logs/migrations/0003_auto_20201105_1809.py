# Generated by Django 3.1.3 on 2020-11-05 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={},
        ),
        migrations.AddField(
            model_name='entry',
            name='topic',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='learning_logs.topic'),
        ),
    ]
