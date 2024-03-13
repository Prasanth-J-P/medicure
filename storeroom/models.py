from django.db import models
class Medicinedetails(models.Model):
    name=models.CharField(max_length=60)
    description=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=8,decimal_places=2)



