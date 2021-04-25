
from django.urls import path
from .views import BlogDeleteView, BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path('register/',RegisterPage.as_view() , name="register"),
    path('login/', CustomLoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('', BlogListView.as_view(), name="home"),
    path('post/<int:pk>/', BlogDetailView.as_view(), name="post_detail" ),
]
