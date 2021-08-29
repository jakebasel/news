from django.urls import path
from .views import ArticleDeleteView, ArticleListView, ArticleCreateView, ArticleUpdateView, ArticleDetailView

urlpatterns = [
    path('', ArticleListView.as_view(), name='articles'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('new/', ArticleCreateView.as_view(), name='create'),
    path('<int:pk>/update', ArticleUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='delete'),
]