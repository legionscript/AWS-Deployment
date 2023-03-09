from django.urls import path, include
from .views import Index, Featured, DeleteArticleView, DetailArticleView, LikeArticle

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('<int:pk>/', DetailArticleView.as_view(), name='detail_article'),
    path('<int:pk>/delete/', DeleteArticleView.as_view(), name='delete_article'),
    path('<int:pk>/like', LikeArticle.as_view(), name='like_article'),
    path('featured/', Featured.as_view(), name='featured'),
    path('tinymce/', include('tinymce.urls')),
]