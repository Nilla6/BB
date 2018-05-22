from django.conf.urls import url, include
from contact.views import ContactView
from . import views

urlpatterns = [
	url(r'^', ContactView.as_view(), name ='Contact'),
	]
