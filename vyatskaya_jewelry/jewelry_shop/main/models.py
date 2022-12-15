from django.db import models



class ChapterTable(models.Model):
    chapter = models.CharField(primary_key=True,max_length=50)
    sum = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chapter_table'


class Collection(models.Model):
    type = models.CharField(max_length=50)
    metal = models.CharField(blank=True, null=True,max_length=50)
    gems = models.CharField(blank=True, null=True,max_length=50)
    mass = models.TextField(blank=True, null=True)  # This field type is a guess.
    price = models.IntegerField(db_column='price ', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    volume_product = models.IntegerField(blank=True, null=True)
    chapter = models.ForeignKey(ChapterTable, models.DO_NOTHING, db_column='chapter', blank=True, null=True)
    photo_kit = models.ForeignKey('Gallary', models.DO_NOTHING, db_column='photo_kit', blank=True, null=True)
    description = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'collection'


class Gallary(models.Model):
    main = models.TextField(blank=True, null=True)  # This field type is a guess.
    minor_1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    minor_2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    minor_3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    minor_4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    minor_5 = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'gallary'


class MethodDeliveryTable(models.Model):
    post = 'post'
    company = 'company'
    person = 'person'
    Met_dev = [
        (post,'почта'),
        (company, 'транспортная компания'),
        (person, 'курьер')
    ]
    method_delivery = models.CharField(primary_key=True,max_length=50)
    price_delivery = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'method_delivery_table'


class Order(models.Model):
    post = 'post'
    company = 'company'
    person = 'person'
    Met_dev = [
        (post, 'почта'),
        (company, 'транспортная компания'),
        (person, 'курьер')
    ]
    order_id = models.AutoField(primary_key=True)
    method_delivery = models.CharField(max_length=10, choices = Met_dev,default=post)
    product = models.ForeignKey(Collection, models.DO_NOTHING, db_column='product', blank=True, null=True)
    price_order = models.IntegerField(blank=True, null=True)
    address = models.CharField(blank=True, null=True,max_length=50)


    class Meta:
        managed = False
        db_table = 'order'


class User(models.Model):
    user_id = models.AutoField(primary_key=True, blank=True, null=False)
    login = models.CharField(blank=True, null=True,max_length=50)
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    surname = models.TextField(blank=True, null=True)  # This field type is a guess.
    petronymic = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


"""class UserOrder(models.Model):
    order = models.ForeignKey(Order, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_order'"""

class GetImage(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='main/img')
    class Meta:
        db_table = "gallary"
