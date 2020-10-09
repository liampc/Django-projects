from django.urls import path 

from .views import (
    HomePageView, 
    BlogListView, 
    BlogCreateView, 
    BlogEditView, 
    BlogDeleteView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/<int:pk>', BlogListView.as_view(), name='post_detail'),
    path('post/new', BlogCreateView.as_view(), name='post_new'),
    path('post/edit/<int:pk>', BlogEditView.as_view(), name='post_edit'),
    path('post/delete/<int:pk>', BlogDeleteView.as_view(), name='post_delete')
]