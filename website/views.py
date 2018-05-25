from django.shortcuts import render, redirect
from website.forms import CreationForm
from django.views.generic import TemplateView
from website.models import Product

# Create your views here.
class CreationView(TemplateView):
	template_name = 'website/creation.html'

	def get(self, request):
		form = CreationForm()
		products = Product.objects.all()
		args = {'form': form, 'products': products}
		return render(request, self.template_name, args)

	def post(self, request):
		form = CreationForm(request.POST, request.FILES)
		if form.is_valid():
			description = form.cleaned_data['description']
			price = form.cleaned_data['price']
			quantity = form.cleaned_data['quantity']
			image = request.FILES['image']
			form.save()
			form = CreationForm()
			return redirect('/')

		args = {'form': form, 'description': description, 'price': price, 'quantity': quantity, 'image': image}
		return render(request, self.template_name, args)

class HomeView(TemplateView):
	template_name = 'website/home.html'

	def get(self, request):
		form = CreationForm()
		products = Product.objects.all()
		args = {'form': form, 'products': products}
		return render(request, self.template_name, args)
