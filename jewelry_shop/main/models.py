
from django.db import models


class ChapterTable(models.Model):
    chapter = models.CharField(primary_key=True, null=False ,max_length=50)
    sum = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chapter_table'


class Collection(models.Model):
    type = models.CharField(primary_key=True, null=False,max_length=50)
    metal = models.CharField(blank=True, null=True,max_length=50)
    gems = models.CharField(blank=True, null=True,max_length=50)
    mass = models.TextField(blank=True, null=True)  # This field type is a guess.
    price_field = models.IntegerField(db_column='price ', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    volume_product = models.IntegerField(blank=True, null=True)
    chapter = models.ForeignKey(ChapterTable, models.DO_NOTHING, db_column='chapter', blank=True, null=True)
    photo = models.TextField(blank=True, null=True)  # This field type is a guess.
    id = models.ForeignKey('Gallary', models.DO_NOTHING, db_column='id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collection'


class Gallary(models.Model):
    title = models.CharField(max_length=50)
    img = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'gallary'
class GetImage(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='main/img')
    class Meta:
        db_table = "gallary"


class MethodDeliveryTable(models.Model):
    method_delivery = models.CharField(primary_key=True, null=False,max_length=50)
    price_delivery = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'method_delivery_table'


class Order(models.Model):
    order_id = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    method_delivery = models.ForeignKey(MethodDeliveryTable, models.DO_NOTHING, db_column='method_delivery', blank=True, null=True)
    product = models.ForeignKey(Collection, models.DO_NOTHING, db_column='product', blank=True, null=True)
    price_order = models.IntegerField(blank=True, null=True)
    address = models.CharField(blank=True, null=True,max_length=50)

    class Meta:
        managed = False
        db_table = 'order'


class User(models.Model):
    user_id = models.TextField(primary_key=True, blank=True, null=False)  # This field type is a guess.
    login = models.CharField(blank=True, null=True,max_length=50)
    order = models.ForeignKey(Order, models.DO_NOTHING, blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'user'