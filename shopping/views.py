from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Product, Store
from django.contrib.auth.decorators import login_required
from .processes import process_purchase

@login_required
def index(request):
    product_list = Product.objects.select_related('store')
    store_list = Store.objects.all()
    context = {
        'product_list': product_list,
        'store_list': store_list,
    }
    return render(request, 'shopping.html', context)


@login_required
def purchase(request, product_id):
    result = process_purchase(product_id)
    return JsonResponse(result)


@login_required
def complete(request, task_id):
    pass


@login_required
def create(request):
    pass


@login_required
def create_store(request):
    pass