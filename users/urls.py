from django.urls import path
from .views import UserRegisterView, UserLoginView, FeedView, HomePageView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('feed/', FeedView.as_view(), name='feed'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]