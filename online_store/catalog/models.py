from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('TS', 'T-shirts'),
        ('SW', 'Sweatshirts'),
        ('PN', 'Pants'),
        ('JC', 'Jackets'),
    ]

    name = models.CharField(max_length=150)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=None)
    article_number = models.CharField(max_length=50, unique=True)
    price = models.FloatField()
    size_s_qty = models.IntegerField(default=0)
    size_m_qty = models.IntegerField(default=0)
    size_l_qty = models.IntegerField(default=0)
    size_xl_qty = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/catalog')