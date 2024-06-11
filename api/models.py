from django.db import models

# Create your models here.
class stock_market(models.Model):
    id=models.AutoField(primary_key=True)
    trade_code = models.CharField(max_length=25)
    high = models.DecimalField(max_digits=5, decimal_places=1)
    low = models.DecimalField(max_digits=5, decimal_places=1)
    open = models.DecimalField(max_digits=5, decimal_places=1)
    close = models.DecimalField(max_digits=5, decimal_places=1)
    volume = models.IntegerField()
    date = models.DateField()
   