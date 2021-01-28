from django.urls import path
from . import views

# from .views import PostListView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_page, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.form, name='form'),
    # path('blog/', PostListView.as_view(), name='blog'),
]
