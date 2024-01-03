from django.shortcuts import render,redirect
from .import forms
# Create your views here.
def add_author(req):
    if req.method=='POST':
        form = forms.AuthorForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('add_author')
    else:
        form = forms.AuthorForm()
    return render(req, 'add_author.html',{'form':form})