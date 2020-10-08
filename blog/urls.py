from django.urls import path 

from .views import HomePageView, BlogListView, BlogCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/<int:pk>', BlogListView.as_view(), name='post_detail'),
    path('post/new', BlogCreateView.as_view(), name='post_new'),
]