# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class GSTServices(models.Model):
	item = models.CharField(max_length = 60)
	tax = models.IntegerField()

class GSTGoods(models.Model):
	item = models.CharField(max_length = 60)
	tax = models.FloatField()

"""
with open('GSTBilling/GST_Services.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        obj = GSTServices(item=row[0],tax=int(row[1]))
        obj.save()

with open('GSTBilling/GST_Goods.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        obj = GSTGoods(item=row[0],tax=float(row[1]))
        obj.save()
"""