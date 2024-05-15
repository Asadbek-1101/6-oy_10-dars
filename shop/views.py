from django.shortcuts import render, get_object_or_404
from .models import Product, Category
def home(request):
    products = Product.objects.all()
    categorys = Category.objects.all()
    return render(request, 'home.html', {"products":products, "cats":categorys})

def category(request, id):
    cat = get_object_or_404(Category, id=id)
    products = cat.products.all()
    categorys = Category.objects.all()
    return render(request, 'home.html', {"products": products, "cats":categorys})

def batafsil(request, id):
    product = get_object_or_404(Product, id=id)
    categorys = Category.objects.all()
    return render(request, 'batafsil.html', {"product": product, "cats": categorys})
