# Generated by Django 4.2.7 on 2024-03-11 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_chart'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='time',
            field=models.DateField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]