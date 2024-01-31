from django.urls import path

from xojiakbar.views import HomePageView, UserLoginView, UserRegisterView, UserLogoutView, AboutView, HomeView, \
    PostFormView, UserPostsView, PostDetailView, PostConfirmDeleteView, UserPostsCreateView

app_name = 'xojiakbar'
urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('about/', AboutView.as_view(), name='about'),
    path('home/', HomeView.as_view(), name='home'),
    path('postform/', PostFormView.as_view(), name='post-form'),
    path('userposts/', UserPostsView.as_view(), name='user-posts'),
    path('postdetail/', PostDetailView.as_view(), name='post-detail'),
    path('postconfirmdelete/', PostConfirmDeleteView.as_view(), name='post-confirm-delete'),
    path('post/create', UserPostsCreateView.as_view(), name='post-create'),
]