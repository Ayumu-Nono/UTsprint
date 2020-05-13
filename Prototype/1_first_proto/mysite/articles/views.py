from django.shortcuts import render
from django.views import generic


class ArticleListView(generic.ListView):
    template_name = 'articles/article_list.html'
