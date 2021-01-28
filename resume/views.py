from django.shortcuts import render
from django.http import HttpResponse
from .models import Resume, Post
from django.views.generic import ListView
from .forms import ContactMe


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about_page(request):
    resume = Resume.objects.get(pk=1)
    return render(request, 'resume/about.html', {'resume': resume})


""" def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'resume/blog.html', context) """


# class PostListView(ListView):
#     model = Post
#     template_name = 'resume/blog.html'
#     context_object_name = 'posts'
#
#     ordering = ['-date']

def blog(request):
    post_objects = Post.objects.all().order_by('-date')
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        post_objects = post_objects.filter(title__icontains=item_name)
    return render(request, 'resume/blog.html', {'post_object': post_objects})


def form(request):
    form = ContactMe
    return render(request, 'resume/form.html', {'form': form})
