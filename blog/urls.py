# blog/urls.py
from django.urls import path
from .views import BlogListView, BlogDetailView, add_post, PostUpdateView, PostDeleteView, add_rating

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', add_post, name='new_post'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/rating/', add_rating, name='add_rating'),  # Updated URL pattern
]
