from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DeleteView, DetailView
from django.views import View
from .models import Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect

class Index(ListView):
    model = Article
    paginate_by = 2
    queryset = Article.objects.all().order_by('-date')
    template_name = 'blog/index.html'

class Featured(ListView):
    model = Article
    paginate_by = 2
    queryset = Article.objects.filter(featured=True).order_by('-date')
    template_name = 'blog/featured.html'

class LikeArticle(View):
    def post(self, request, pk):
        article = Article.objects.get(id=pk)
        if article.likes.filter(pk=self.request.user.id).exists():
            article.likes.remove(request.user.id)
        else:
            article.likes.add(request.user.id)

        article.save()
        return redirect('detail_article', pk)

class DetailArticleView(DetailView):
    model = Article
    template_name = 'blog/blog_post.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailArticleView, self).get_context_data(*args, **kwargs)
        context['liked_by_user'] = False
        article = Article.objects.get(id=self.kwargs.get('pk'))
        if article.likes.filter(pk=self.request.user.id).exists():
            context['liked_by_user'] = True
        return context

class DeleteArticleView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('index')
    template_name = 'blog/blog_delete.html'

    def test_func(self):
        return self.request.user.id == self.kwargs.get('pk')