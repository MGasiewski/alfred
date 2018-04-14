from .models import Product


def process_purchase(product_id):
    count = Product.objects.filter(id=product_id).update(purchased=False)
    return {"result": "success"} if count == 1 else {"result": "failure"}