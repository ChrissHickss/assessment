from django.shortcuts import render, redirect
from .models import Category, Post
from .forms import CategoryForm, PostForm
import datetime


# Category functions

def get_category(category_id):
    return Category.objects.get(id=category_id)

def category_list(request):
    categories = Category.objects.all()
    data = {
        'all_categories': categories,
        'title': 'category List'
    }
    return render(request, 'craigslist/category_list.html', data)

def new_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_detail', category_id=category.id)
    else:
        form = CategoryForm()
        return render(request, 'craigslist/category_form.html', {
            'form': form,
            'type_of_request': 'New'
        })

def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    data = {
        'category': category
    }
    return render(request, 'craigslist/category_detail.html', data)

def edit_category(request, category_id):
    category = get_category(category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_detail', category_id=category.id)
    else:
        form = CategoryForm(instance=category)
        return render(request, 'craigslist/category_form.html', {
            'form': form,
            'type_of_request': 'Edit'
        })

def delete_category(request, category_id):
    category = get_category(category_id=category_id)
    category.delete()
    return redirect('category_list')


#Post functions

def post_detail(request, category_id, post_id):
    category = get_category(category_id)
    post = Post.objects.get(id=post_id)
    return render(request, 'craigslist/post_detail.html', {'category': category, 'post': post})

def new_post(request, category_id):
    category = get_category(category_id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.category = category
            post.save()
            return redirect('post_detail', category_id=category.id, post_id=post.id)
    else:
        form = PostForm({'category': category})
        return render(request, 'craigslist/post_form.html', {
            'form': form,
            'type_of_request': 'New'
        })


def edit_post(request, category_id, post_id):
    category = get_category(category_id)
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', category_id=category.id, post_id=post.id)
    else:
        form = PostForm(instance=post)
        return render(request, 'craigslist/post_form.html', {
            'form': form,
            'type_of_request': 'Edit'
        })

def delete_post(request, category_id, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('category_detail', category_id=category_id)