from django.urls import path
from .views import UserRegisterView, UserEditView, \
    PasswordsChangeView, password_success, ShowProfileView, EditProfileView, CreateProfileView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('edit_profile/', UserEditView.as_view(), name = 'edit_profile'),
    path('password/', PasswordsChangeView.as_view(), name='change_password'),
    path('password_success/', password_success, name="password_changed_success"),
    path('<int:pk>/profile/', ShowProfileView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile/', EditProfileView.as_view(), name='eidt_profile_page'),
    path('create_profile/', CreateProfileView.as_view(), name='create_profile_page'),

]