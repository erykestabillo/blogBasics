# Generated by Django 2.0.13 on 2019-10-03 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0005_auto_20191003_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='content',
        ),
        migrations.AddField(
            model_name='content',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userApp.Category'),
        ),
    ]
