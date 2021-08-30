from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, \
    UpdateCategoryView, DeleteCategoryView, CategoryDetailView, CategoryListView, LikeView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name= 'add-post'),
    path('add_category/', AddCategoryView.as_view(), name= 'add-category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name = 'update-post'),
    path('category/edit/<int:pk>', UpdateCategoryView.as_view(), name = 'update-category'),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name = 'delete-post'),
    path('category/delete/<int:pk>', DeleteCategoryView.as_view(), name = 'delete-category'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name = 'category-detail'),
    path('category-list/', CategoryListView.as_view(), name = 'category-list'),
    path('like/<int:pk>', LikeView, name = 'like_post'),

]