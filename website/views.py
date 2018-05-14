from django.shortcuts import render
from django.http import HttpResponse
from website.forms import CreationForm
#from django.views.generic import TemplateView

# Create your views here.
def home(request):
	return render(request, 'website/home.html')

def creation(request):
	return render(request, 'website/creation.html')

#class HomeView(TemplateView):
	#template_name = 'website/home.html'
def get(self, request):
	form = CreationForm()
	return render(request, 'website/creation.html', {'form': form})
