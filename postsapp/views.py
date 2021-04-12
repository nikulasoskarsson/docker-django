from django.shortcuts import render
from .models import Post


def getPosts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'testing': 'testing'
    }
    return render(request, 'posts/posts.html', context)


def getSinglePost(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'posts/single-post.html', context)


def addPost(request):
    if request.method == 'GET':
        return render(request, 'posts/add-post.html')
    elif request.method == 'POST':
        Post.objects.create(
            title=request.POST['title'],
            body=request.POST['title'],
        )
        context = {
            'post_added': 'Post has been added'
        }
        return render(request, 'posts/add-post.html', context)


def updatePost(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(pk=post_id)
        context = {
            'post': post
        }
        return render(request, 'posts/update-post.html', context)

    elif request.method == 'POST':
        post = Post.objects.filter(pk=post_id)
        post.update(
            title=request.POST['title'],
            body=request.POST['body'],
        )

        context = {
            'post_updated': 'Post has been updated'
        }

        return render(request, 'posts/posts.html', context)


def deletePost(request, post_id):
    Post.objects.filter(pk=post_id).delete()

    context = {
        'post_deleted': 'Post has been deleted'
    }

    return render(request, 'posts/posts.html', context)
