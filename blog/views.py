from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Post

# Create your views here.

class HomePageView(ListView):
    template_name = 'home.html'
    model = Post


class DetailsView(DetailView):
    template_name = 'post_detail.html'
    model = Post
