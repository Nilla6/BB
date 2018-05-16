from django.shortcuts import render, redirect
from website.forms import CreationForm
from django.views.generic import TemplateView
from website.models import Products

# Create your views here.
class CreationView(TemplateView):
	template_name = 'website/creation.html'

	def get(self, request):
		form = CreationForm()
		products = Products.objects.all()

		args = {'form': form, 'products': products}
		return render(request, self.template_name, args)

	def post(self, request):
		form = CreationForm(request.POST)
		if form.is_valid():
			form.save()
			description = form.cleaned_data['description']
			price = form.cleaned_data['price']
			quantity = form.cleaned_data['quantity']
			form = CreationForm()
			return redirect('/')

		args = {'form': form, 'description': description, 'price': price, 'quantity': quantity}
		return render(request, self.template_name, args)

class HomeView(TemplateView):
	template_name = 'website/home.html'
