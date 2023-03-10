# Generated by Django 4.1.7 on 2023-03-07 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size_l_qty',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size_m_qty',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size_s_qty',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size_xl_qty',
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
