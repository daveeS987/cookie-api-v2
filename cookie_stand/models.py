from django.db import models
from django.conf import settings
import random


class Cookie_Stand(models.Model):
    # title = models.CharField(max_length=64)
    # body = models.TextField(max_length=256)
    # # slug = models.SlugField(max_length=64, unique=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=256)
    description = models.TextField(default="", null=True, blank=True)
    hourly_sales = models.JSONField(default=list, blank=True)
    minimum_customers_per_hour = models.IntegerField(default=0)
    maximum_customers_per_hour = models.IntegerField(default=0)
    average_cookies_per_sale = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location

    def save(self, *args, **kwargs):

        if not self.pk and not self.hourly_sales:
            min = self.minimum_customers_per_hour
            max = self.maximum_customers_per_hour

            cookies_each_hour = [int(random.randint(min, max) * self.average_cookies_per_sale) for _ in range(14)]

            self.hourly_sales = cookies_each_hour

        super().save(*args, **kwargs)
