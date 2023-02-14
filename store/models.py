from django.db import models
from django.conf import settings
from django.contrib import admin
# Create your models here.


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]

    brith_date = models.DateField(null=True, blank=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__last_name']


# class Order(models.Model):
    # PAYMENT_STATUS_PENDING = 'p'
    # PAYMENT_STATUS_COMPLETE = 'C'
    # PAYMENT_STATUS_FAILED = 'F'
    # PAYMENT_STATUS_CHOICES = [

    # ]

    # def __str__(self):
    #     pass

    # class Meta:
    #     db_table = ''
    #     managed = True
    #     verbose_name = 'Order'
    #     verbose_name_plural = 'Orders'
# collection, orderitem, product, product_pormotions, pormotion, review, cartItems,cart, address
