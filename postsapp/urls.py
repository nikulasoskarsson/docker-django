from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.getPosts, name='index'),
    path('posts/<int:post_id>/', views.getSinglePost, name='single'),
    path('add-post', views.addPost, name='add'),
    path('posts/update/<int:post_id>', views.updatePost, name='update'),
    path('posts/delete/<int:post_id>', views.deletePost, name='delete'),
]
