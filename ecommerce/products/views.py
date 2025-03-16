from django.shortcuts import render,get_object_or_404
from .models import Product,Category


#data
# products=[{"id":1,"name":"Phone","price":200,"summary":"This is a phone"},
# {"id":2,"name":"Laptop","price":1000,"summary":"This is a laptop"},
# {"id":3,"name":"Keyboard","price":20,"summary":"This is a keyboard"}]



# Create your views here.
def product_list(request):
    products=Product.objects.all()
    return render(request, 'product_list.html',{"products":products})

def product_detail(request,id):
    products=get_object_or_404(Product,id=id)
    return render(request, 'product_detail.html',{"products":products})

def category_list(request):
    categories=Category.objects.all()
    return render (request, 'category_list.html',{"categories":categories})


def category_detail(request,id):
    category=get_object_or_404(Category,id=id)
    products=category.products.all()
    return render(request,'category_detail.html',{"category":category,"products":products})

