from django.urls import path
from .views import UserRegisterView, UserLoginView, FeedView, HomePageView, UserProfileUpdateView, UserProfileDeleteView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('feed/', FeedView.as_view(), name='feed'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/edit/', UserProfileUpdateView.as_view(), name='profile_edit'),
    path('profile/delete/', UserProfileDeleteView.as_view(), name='profile_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)