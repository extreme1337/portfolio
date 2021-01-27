from django.shortcuts import render
from django.http import HttpResponse
from .models import Resume

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about_page(request):
    resume = Resume.objects.get(pk=1)
    return render(request, 'resume/about.html', {'resume': resume})
