from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Product, Store
from django.contrib.auth.decorators import login_required
from .processes import process_purchase, process_create, process_clear_list, process_create_store, process_delete_product, process_edit_product

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
def clear_list(request, store_id):
    result = process_clear_list(store_id)
    return JsonResponse(result)


@login_required
def create(request):
    result = process_create(request)
    return JsonResponse(result)

@login_required
def create_store(request):
    result = process_create_store(request)
    return JsonResponse(result)

@login_required
def delete_product(request, product_id):
    result = process_delete_product(product_id)
    return JsonResponse(result)

@login_required
def update(request, product_id):
    result = process_edit_product(request, product_id)
    return  JsonResponse(result)