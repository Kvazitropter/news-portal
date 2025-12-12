from django.views import View
from django.shortcuts import render, get_object_or_404

from news_portal.news.models import NewsArticle


class NewsMainPageView(View):
    def get(self, request):
        search_query = request.GET.get('search_query', '')
        include_unpublished = request.GET.get('include_unpublished')
        print(request.GET)
        news = NewsArticle.objects \
            .all() \
            .filter(title__iregex=f'(?i){search_query}') \
            .order_by('-created_at')
        if not include_unpublished:
            news = news.filter(is_published=True)
        return render(
            request,
            'news/base_news.html',
            context={
                'news': news,
                'search_query': search_query,
                'include_unpublished': include_unpublished,
            },
        )


class NewsPageView(View):
    def get(self, request, news_id):
        news_article = get_object_or_404(NewsArticle, id=news_id)
        return render(
            request,
            'news/news_article.html',
            context={
                'news_article': news_article,
            },
        )
