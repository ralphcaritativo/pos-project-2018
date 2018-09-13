# Generated by Django 2.0.8 on 2018-09-12 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0003_auto_20180912_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='is_active',
            field=models.BooleanField(choices=[(0, False), (1, True)], default=1),
        ),
        migrations.AlterField(
            model_name='brand',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
