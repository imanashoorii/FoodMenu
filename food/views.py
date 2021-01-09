from django.shortcuts import render, redirect
from .models import Product
from django.http import HttpResponseRedirect
from .forms import AddItemForm


# Create your views here.

def index(request):
    product_qs = Product.objects.all()

    context = {
        'product_qs': product_qs,
    }
    return render(request, 'home.html', context)


def delete_item(request, product_id):
    Product.objects.get(id=product_id).delete()
    return HttpResponseRedirect("/")


def detail_view(request, product_id):
    id_qs = Product.objects.get(pk=product_id)

    context_processors = {
        'id_qs': id_qs,
    }

    return render(request, 'detail.html', context_processors)


def add_product(request):
    form = AddItemForm(request.POST or None, request.FILES)

    if form.is_valid():
        # title = request.POST.get('title')
        # description = request.POST.get('description')
        # price = request.POST.get('price')
        # image = request.POST.get('image')
        form.save()
        return redirect("food:home")

    return render(request, 'index.html', {'form': form})


def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    form = AddItemForm(request.POST or None, request.FILES, instance=product)

    if form.is_valid():
        form.save()
        return redirect('food:home')

    return render(request, 'add-item.html', {'form': form, 'product': product})
