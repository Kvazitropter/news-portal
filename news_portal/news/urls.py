from django.urls import path

from news_portal.news import views


urlpatterns = [
    path('', views.NewsMainPageView.as_view(), name='news'),
    path('<int:news_id>/', views.NewsPageView.as_view(), name='news_article')
]
