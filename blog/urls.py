from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_posts, name='blog_main'),
    path('new_post/', views.new_post, name='new_post'),
    path('edit_post_entry/<slug:slug>/', views.edit_post_entry,
         name='edit_post_entry'),
    path('delete_post/<slug:slug>/', views.delete_blog_post,
         name='delete_blog_post'),
    path('<slug:slug>/', views.blog_descriptions, name='blog_descriptions'),
]