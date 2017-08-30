from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^home/', views.home, name="GSTBillingHome"),
	url(r'^GSTCompute/', views.calculateTax, name="GSTCompute")
]