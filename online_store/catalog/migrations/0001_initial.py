# Generated by Django 4.1.7 on 2023-03-06 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('category', models.CharField(choices=[('TS', 'T-shirts'), ('SW', 'Sweatshirts'), ('PN', 'Pants'), ('JC', 'Jackets')], default=None, max_length=2)),
                ('article_number', models.CharField(max_length=50, unique=True)),
                ('price', models.FloatField()),
                ('size_s_qty', models.IntegerField(default=0)),
                ('size_m_qty', models.IntegerField(default=0)),
                ('size_l_qty', models.IntegerField(default=0)),
                ('size_xl_qty', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='images/catalog')),
            ],
        ),
    ]
