from django import forms
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from .models import Category
from .forms import CategoryForm
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)


def list_view(request):
    context ={}
    context["dataset"] = Category.objects.all()
    return render(request, "blog/index.html", context)

def create_view(request):
    context ={}
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context['form']= form
    return render(request, "blog/create_view.html", context)

def detail_view(request, id):
    data = Category.objects.get(id = id)
    if request.method == 'POST':
        form = CategoryRequestForm(request.POST)
        if form.is_valid():
            waktu = form.cleaned_data['waktu']
            print("waktu: ", waktu)
            data.available = False
            data.save()
    
    form = CategoryRequestForm()
    return render(request, "blog/detail_view.html", locals())

def update_view(request, id):
    context ={}
    obj = get_object_or_404(Category, id = id)
    form = CategoryForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
  
    context["form"] = form
    return render(request, "blog/update_view.html", context)

def delete_view(request, id):
    context ={}
    obj = get_object_or_404(Category, id = id)
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "blog/delete_view.html", context)

def pesan_category(request, id):
    obj= Category.objects.get(pk=id)
    obj.available = False
    # TODO: Ketika proses update harusnya ada field updated_at (kapan di update)
    obj.save()
    return redirect('/', id)

def batalpesan_category(request, id):
    obj= Category.objects.get(id=id)
    obj.available = True
    # TODO: Ketika proses update harusnya ada field updated_at (kapan di update)
    obj.save()
    

    return redirect('/', id)

class CategoryRequestForm(forms.Form):
    waktu = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"Masukkan waktu",
                "onchange":"print_text()",
            }
        )
    )