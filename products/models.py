from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):

    DRUG_CATEGORIES = (
        ('Analgesics/Pain Relievers', 'Analgesics/Pain Relievers'),
        ('Antibiotics', 'Antibiotics'),
        ('Antidepressants', 'Antidepressants'),
        ('Antihistamines', 'Antihistamines'),
        ('Antihypertensives', 'Antihypertensives'),
        ('Anti-inflammatory Drugs', 'Anti-inflammatory Drugs'),
        ('Antacids', 'Antacids'),
        ('Anticoagulants', 'Anticoagulants'),
        ('Asthma Medications', 'Asthma Medications'),
        ('Diabetes Medications', 'Diabetes Medications'),
    )
    name = models.CharField(max_length = 50,choices=DRUG_CATEGORIES, null = True, blank = True)
    def __str__(self):
        return self.name


class Product(models.Model):
    category_name = models.ForeignKey(Category, on_delete = models.CASCADE,null = True, blank = True )
    item_name = models.CharField(max_length = 50, null = True, blank = True)
    total_quantity = models.IntegerField(default = 0, null = True, blank = True)
    issued_quantity = models.IntegerField(default = 0, null = True, blank = True)
    received_quantity = models.IntegerField(default = 0, null = True, blank = True)
    unit_price = models.IntegerField(default = 0, null = True, blank = True)

    def __str__(self):
        return self.item_name

  

class Sale(models.Model):
    item = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 0, null = True, blank = True)
    amount_received = models.IntegerField(default = 0, null = True, blank = True)
    issued_to = models.CharField(max_length = 50, null = True, blank = True)
    unit_price = models.IntegerField(default = 0, null = True, blank = True)

    def get_total(self):
        total = self.quantity * self.item.unit_price
        return int(total)
    
    def get_change(self):
        change = self.get_total() - self.amount_received
        return abs(int(change))

    
    def __str__(self):
        return self.item.item_name

