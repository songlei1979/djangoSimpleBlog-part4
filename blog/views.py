from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from blog.models import Post, Category
from .forms import PostForm, EditForm


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = Category.objects.all()
    #     context = super(HomeView, self).get_context_data(**kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_detail.html"
    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = Category.objects.all()
    #     context = super(HomeView, self).get_context_data(**kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title', 'body')
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    # fields = ('title', 'body')

class UpdateCategoryView(UpdateView):
    model = Category
    # form_class = EditForm
    template_name = 'update_category.html'
    # fields = ['title', 'title_tag', 'body']

class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'delete_category.html'
    success_url = reverse_lazy('home')

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category.html'

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'