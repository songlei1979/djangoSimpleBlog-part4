from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from blog.models import Post, Category, Profile, Comment
from .forms import PostForm, EditForm, AddCommentForm
from django.http import HttpResponseRedirect


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
    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["total_likes"] = post.total_likes()
        context["liked"] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title', 'body')
    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = Category.objects.all()
    #     context = super(AddPostView, self).get_context_data(**kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context

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

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid((form))

    # success_url = reverse_lazy('/article-detail/'+str(getPostID()))

def search_post(request):
    if request.method == 'POST':
        search_target = request.POST['search_target']
        posts = Post.objects.filter(title__contains=search_target)
        return render(request, 'searchresult.html',
                      {'search_target':search_target,
                       'posts':posts})
    else:
        return render(request, 'searchresult.html', {})