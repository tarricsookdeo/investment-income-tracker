from django.db import models


class Position(models.Model):
    ticker = models.CharField(max_length=5)
    shares = models.DecimalField(max_digits=10, decimal_places=6)
    avg_price_per_share = models.DecimalField(max_digits=9, decimal_places=3)

    def __str__(self):
        return self.ticker
