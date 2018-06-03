from .models import Product, Store

SUCCESS = {"result": "success"}
FAILURE = {"result": "failure"}


def process_purchase(product_id):
    prod = Product.objects.get(id=product_id)
    count = Product.objects.filter(id=product_id).update(purchased=not prod.purchased)
    return SUCCESS if count == 1 else FAILURE


def process_create(request):
    req_product_name = request.POST["productName"]
    req_quantity = request.POST["productQuantity"]
    req_store_name = request.POST["productStoreName"]
    store = Store.objects.get(sname=req_store_name)
    count = Product.objects.create(pname=req_product_name, quantity=req_quantity, store=store)
    return SUCCESS if count == 1 else FAILURE

def process_delete_product(product_id):
    prod = Product.objects.get(id=product_id)
    prod.delete()
    return SUCCESS

def process_edit_product(product_id, product_name, product_quantity, product_store):
    store = Store.objects.get(sname=product_store.replace("-", "/"))
    prod = Product.objects.get(id=product_id)
    prod.pname = product_name
    prod.quantity = product_quantity
    prod.store = store
    prod.save()
    return SUCCESS

def process_clear_list(store_id):
    s = Store.objects.get(id=store_id)
    result = Product.objects.filter(store=s, purchased=True).update(completed=True)
    return SUCCESS


def process_create_store(request):
    req_product_name = request.POST["storeName"]
    count = Store.objects.create(sname=req_product_name)
    return SUCCESS if count == 1 else FAILURE

