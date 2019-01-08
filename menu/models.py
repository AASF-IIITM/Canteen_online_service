from django.db import models


class Menu(models.Model):
    category = models.CharField(max_length=50)
    image = models.ImageField()

    def __str__(self):
        return self.category


class Vegetable(models.Model):
    vegetable = models.CharField(max_length=50)
    vegetable_image = models.FileField()
    vegetable_amt = models.FloatField(default=0)

    def __str__(self):
        return '{}{}'.format(self.vegetable, self.vegetable_amt)


class Thali(models.Model):
    thali = models.CharField(max_length=50)
    thali_image = models.FileField()
    thali_amt = models.FloatField(default=0)

    def __str__(self):
        return '{}{}'.format(self.thali, self.thali_amt)


class Breads(models.Model):
    breads = models.CharField(max_length=50)
    breads_image = models.FileField()
    breads_amt = models.FloatField(default=0)

    def __str__(self):
        return '{}{}'.format(self.breads, self.breads_amt)


class Snacks(models.Model):
    snacks = models.CharField(max_length=50)
    snacks_image = models.FileField()
    snacks_amt = models.FloatField(default=0)

    def __str__(self):
        return '{}{}'.format(self.snacks, self.snacks_amt)


class StreetFood(models.Model):
    streetfood = models.CharField(max_length=50)
    streetfood_image = models.FileField()
    streetfood_amt = models.FloatField(default=0)

    def __str__(self):
        return '{}{}'.format(self.streetfood, self.streetfood_amt)


class Beverages(models.Model):
    beverages = models.CharField(max_length=50)
    beverages_image = models.FileField()
    beverages_amt = models.FloatField(default=0)

    def __str__(self):
        return '{}{}'.format(self.beverages, self.beverages_amt)


class Desserts(models.Model):
    desserts = models.CharField(max_length=50)
    desserts_image = models.FileField()
    desserts_amt = models.FloatField(default=0)

    def __str__(self):
        return '{}{}'.format(self.desserts, self.desserts_amt)


class Rice(models.Model):
    rice = models.CharField(max_length=50)
    rice_image = models.FileField()
    rice_amt = models.FloatField(default=0)

    def __str__(self):
        return '{}{}'.format(self.rice, self.rice_amt)




