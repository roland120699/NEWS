from django.shortcuts import render, get_list_or_404
from .models import Article

def news_list(requests):
    articles = Article.objects.order_by('-pub_date')
    return render(requests, 'news/news_list.html', {'articles': articles})

def article_detail(requests, article_id):
    article = get_list_or_404(Article, pk=article_id)
    return render(requests, 'news/news_list.html', {'articles': articles})
