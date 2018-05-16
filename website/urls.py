from django.conf.urls import url
from website.views import HomeView, CreationView
from . import views

# Create your views here.
urlpatterns = [
	url(r'^$', HomeView.as_view(), name ='Home'),
	url(r'^creation/', CreationView.as_view(), name ='Creation Page'),
	]
