# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from models import GSTServices

servicesList = GSTServices.objects.all()

# Create your views here.
def home(request):
	items = [i for i in range(5)]
	context = {'data': servicesList, 
			   'itemCount': items}

	return render(request, 'GSTBilling/home.html',context)

def calculateTax(request):
	listSize = 5
	data = request.GET
	tax = GSTServices.objects.get(item = data['service']).tax
	items = [i for i in range(listSize)]
	userData = []
	sumCost = 0
	company = data['company']
	for i in range(listSize):
		tempData = {}
		tempData['itemName'] = data['itemName'+str(i)]
		if(tempData['itemName'] == ''): continue
		tempData['qty'] = data['qty'+str(i)]
		tempData['price'] = data['price'+str(i)]
		sumCost += int(data['qty'+str(i)]) * int(data['price'+str(i)])
		userData.append(tempData)

	# return HttpResponse(userData)
	taxAmount = float(sumCost*tax)/100.0
	totalAmount = sumCost + taxAmount 

	context = {'company':company,
			   'data': userData, 
			   'itemCount': items,
			   'result' : str(tax),
			   'Sum': sumCost,
			   'Tax': taxAmount,
			   'Total':totalAmount,
			   't':tax}

	return render(request, 'GSTBilling/bill.html',context)