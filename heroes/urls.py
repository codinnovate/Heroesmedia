from django.urls import path
from .views import (HomePageView,
	ArticleListView,
	ArticleCreateView,
	ArticleDetailView,
	ArticleUpdateView,
	ArticleDeleteView,
)
urlpatterns = [
  path('article/<int:pk>/delete/',
  	ArticleDeleteView.as_view(), name='articledelete'),
  path('',HomePageView.as_view(), name='home'),
  path('article/new/',ArticleCreateView.as_view(),name= 'article_new'),
  path('Article/<int:pk>/',ArticleDetailView.as_view(),name='article'), 
  path('article/<int:pk>/edit/',
  	ArticleUpdateView.as_view(), name='article_edit'),

  path('',ArticleListView.as_view(), name='home'),
]