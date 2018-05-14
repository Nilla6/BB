from django.conf.urls import url
from . import views

# Create your views here.
urlpatterns = [
	url(r'^$', views.home, name ='Home'),
	url(r'^creation/', views.creation, name ='Creation Page'),
	]