from django.db import models


class Store(models.Model):
    sname = models.CharField(max_length=200)

    def __str__(self):
        return self.sname


class Product(models.Model):
    quantity = models.IntegerField(default=1)
    pname = models.CharField(max_length=200)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, default=1)
    completed = models.BooleanField(default=False)
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return str(self.quantity) + " " + self.pname

    @property
    def fmt_completed(self):
        return "true" if self.completed else "false"

    @property
    def fmt_purchased(self):
        return "true" if self.purchased else "false"
