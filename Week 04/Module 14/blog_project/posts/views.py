from django.shortcuts import render, redirect
from .import forms
from  .import models
# Create your views here.


def add_post(req):
    if req.method == 'POST':
        form = forms.PostForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('add_post')
    else:
        form = forms.PostForm()
    return render(req, 'add_post.html', {'form':form})


def edit_post(req,id):

    post = models.Post.objects.get(pk=id)
    form = forms.PostForm(instance=post)
    if req.method == 'POST':
        form = forms.PostForm(req.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(req, 'add_post.html', {'form': form})
def delete_post(req,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect("homepage")