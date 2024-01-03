from django.shortcuts import render, redirect
from .import forms
# Create your views here.


def add_category(req):
    if req.method == 'POST':
        form = forms.CategoryForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('add_category')
    else:
        form = forms.CategoryForm()
    return render(req, 'add_category.html', {'form':form})