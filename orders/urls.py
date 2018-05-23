from django.conf.urls import url
from orders.views import CheckoutView, ConfirmationView, CartView
from . import views

# Create your views here.
urlpatterns = [
	url(r'^checkout/', CheckoutView.as_view(), name ='Checkout Page'),
	url(r'^confirmation/', ConfirmationView.as_view(), name = 'Order Confirmation Page'),
	url(r'^cart/', CartView.as_view(), name = 'Shopping Cart Page')
]
