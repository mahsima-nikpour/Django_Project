from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def product_list_view(request: HttpRequest):
    context = {
        "products": [
            {'id': 1, 'name': "iphone", 'price': 1000},
            {'id': 2, 'name': "mc", 'price': 1001},
            {'id': 3, 'name': "ipad", 'price': 1002}, ]
    }
    return render(request, template_name='product/product.html', context=context)


def product_detail_view(request: HttpRequest):
    return render(request, "product/detail.html")


def home(request):
    return render(request, "product/home.html")
