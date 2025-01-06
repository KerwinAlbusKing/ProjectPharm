from django.db import models

# Create your models here.

class InsuranceItem(models.Model):
    insurance_code = models.CharField(max_length=20, primary_key=True, verbose_name="보험코드")
    name = models.CharField(max_length=100, verbose_name="품명")
    specification = models.CharField(max_length=100, verbose_name="규격")
    quantity = models.IntegerField(verbose_name="수량")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="단가")
    total_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="금액")
    expiry_date = models.DateField(verbose_name="유효기간")

    def __str__(self):
        return f"{self.insurance_code} - {self.name}"
