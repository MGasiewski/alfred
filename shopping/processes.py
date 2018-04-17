from .models import Product, Store

SUCCESS = {"result": "success"}
FAILURE = {"result": "failure"}


def process_purchase(product_id: int):
    count = Product.objects.filter(id=product_id).update(purchased=True)
    return SUCCESS if count == 1 else FAILURE


def process_create(request):
    req_product_name = request.POST["productName"]
    req_quantity = request.POST["productQuantity"]
    req_store_name = request.POST["productStoreName"]
    store = Store.objects.get(sname=req_store_name)
    count = Product.objects.create(pname=req_product_name, quantity=req_quantity, store=store)
    return SUCCESS if count == 1 else FAILURE


def process_clear_list(store_id: int):
    s = Store.objects.get(id=store_id)
    result = Product.objects.filter(store=s).update(completed=True)
    return SUCCESS


def process_create_store(request):
    req_product_name = request.POST["storeName"]
    count = Store.objects.create(sname=req_product_name)
    return SUCCESS if count == 1 else FAILURE
