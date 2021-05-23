from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from .models import Article,Comment
from django.urls import reverse_lazy

class HomePageView(TemplateView):
	template_name = 'home.html'

class ArticleListView(ListView):
	model = Article
	template_name = 'home.html'

class ArticleDetailView(DetailView):
	model = Article
	template_name = 'article.html'

class ArticleCreateView(CreateView):
	model = Article
	template_name = 'article_new.html'
	fields = '__all__'

class ArticleUpdateView(UpdateView):
	model=Article
	template_name="article_edit.html"
	fields=['title','body','image']

class ArticleDeleteView(DeleteView):
	model = Article
	template_name='articledelete.html'
	success_url=reverse_lazy('home')
