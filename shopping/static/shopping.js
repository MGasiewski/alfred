class Product{
  constructor(id, name, quantity, purchased, completed, storeName){
    this.id = id;
    this.name = name;
    this.quantity = quantity;
    this.purchased = purchased;
    this.completed = completed;
    this.storeName = storeName;
  }
}

function attachCheckCallbacks(){
productList.forEach(function(product){
    $("#purchased_button_" + product.id).unbind();
    $("#purchased_button_" + product.id).click(function(){
        $("#product_name_" + product.id).css("text-decoration", "line-through");
        $("#product_quantity_" + product.id).css("text-decoration", "line-through");
        });
    });
}

$(document).ready(function(){
    attachCheckCallbacks();
});