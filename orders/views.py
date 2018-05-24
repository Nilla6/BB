from django.shortcuts import render, redirect
from orders.forms import OrderForm
from django.views.generic import TemplateView
from orders.models import Order
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
class CheckoutView(TemplateView):
    template_name = 'orders/checkout.html'

    def get(self, request):
        form = OrderForm()
        orders = Order.objects.all()
        args = {'form': form, 'orders': orders}
        return render(request, self.template_name, args)

    def post(self, request):
        if request.method == "POST":
            form = OrderForm(request.POST)
            publishable = settings.STRIPE_PUBLISHABLE_KEY
            if form.is_valid():
                fname = form.cleaned_data['fname']
                lname = form.cleaned_data['lname']
                email = form.cleaned_data['email']
                address = form.cleaned_data['address']
                address2 = form.cleaned_data['address2']
                postal_code = form.cleaned_data['postal_code']
                city = form.cleaned_data['city']
                state = form.cleaned_data['state']
                country = form.cleaned_data['country']
                try:
                    customer = stripe.Charge.create(
                        amount = 499,
                        currency = "USD",
                        description = email,
                        card = form.cleaned_data['stripe_id'],
                    )
                    form.save()
                    redirect('confirmation/')
                except:
                    print("Card Declined")

        args = {'form': form, 'fname': fname, 'lname': lname, 'email': email, 'address': address, 'postal_code': postal_code, 'city': city, 'state': state, 'country': country, 'publishable': publishable}
        return render(request, self.template_name, args)

class ConfirmationView(TemplateView):
    template_name = 'orders/confirmation.html'

class CartView(TemplateView):
    template_name = 'orders/cart.html'
