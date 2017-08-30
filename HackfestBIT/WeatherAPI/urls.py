from django.conf.urls import url, include
import views
urlpatterns = [
	url(r'^home/',views.home),
	url(r'^get/',views.weather,name="getweather"),
]