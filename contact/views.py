from django.shortcuts import render, redirect
from contact.forms import ContactMeForm
from django.views.generic import TemplateView
from contact.models import ContactMe

# Create your views here.
class ContactView(TemplateView):
	template_name = 'contact/contact.html'

	def get(self, request):
		form = ContactMeForm()
		contact = ContactMe.objects.all()
		args = {'form': form, 'contact': contact}
		return render(request, self.template_name, args)

	def post(self, request):
		form = ContactMeForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			description = form.cleaned_data['description']
			form.save()
			form = ContactMeForm()

		args = {'form': form, 'name': name, 'email': email, 'description': description}
		return render(request, self.template_name, args)
