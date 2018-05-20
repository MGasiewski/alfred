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

class Store{
  constructor(id, name){
    this.id = id;
    this.name = name;
  }
}

function attachDeleteCallbacks(){
  productList.forEach(function(product){
    $("#deleted_button_" + product.id).unbind();
    $("#deleted_button_" + product.id).click(function(){
      deleteItem(product.id);
    });
  });
}

function deleteItem(prod_id){
  $.ajax({
    url: "delete/" + prod_id + "/",
    method: "POST",
    data:{
      csrfmiddlewaretoken: csrfToken
    }
  }).done(function(data){
    window.location.reload();
    //TODO implement failure behavior
  });
}

function attachCheckCallbacks(){
    productList.forEach(function(product){
        $("#purchased_button_" + product.id).unbind();
        $("#purchased_button_" + product.id).click(function(){
            strikeProduct(product.id);
            markPurchased(product.id);
        });
    });
}

function attachClearListCallbacks(){
    storeList.forEach(s => {
        console.log(s);
        $("#clear_list_" + s.id).unbind();
        $("#clear_list_" + s.id).click(function(){
            $("#clear_list_button").unbind();
            $("#clear_list_button").click(function(){
                clearList(s.id);
            });
        });
    });
}

function clearList(store_id){
    $.ajax({
        url: "clear_list/" + store_id + "/",
        method: "POST",
        data:{
            csrfmiddlewaretoken: csrfToken
        }
    }).done(function(data){
        if(data["result"] == "failure"){
            //TODO implement failure behavior
            console.log("failed to update record");
        }else{
            window.location.reload();
        }
    });
}

function strikePurchasedProducts(){
    productList.filter(product => product.purchased)
               .forEach(function(product){
                strikeProduct(product.id);
               });
}

function strikeProduct(product_id){
    $("#product_name_" + product_id).css("text-decoration", "line-through");
    $("#product_quantity_" + product_id).css("text-decoration", "line-through");
}

function markPurchased(product_id){
    $.ajax({
        url: "purchase/" + product_id + "/",
        method: "POST",
        data:{
            csrfmiddlewaretoken: csrfToken
        }
    }).done(function(data){
        if(data["result"] == "failure"){
            //TODO implement failure behavior
            console.log("failed to update record");
        }
    });
}

function attachSetDefaultStoreCallbacks(){
    storeList.forEach(s => {
        $("#add_product_button_" + s.id).unbind();
        $("#add_product_button_" + s.id).click(function(){
            $("#store_name").val(s.id);
        });
    });
}

function addStore(storeName){
    $.ajax({
        url: "create_store/",
        method: "POST",
        data:{
            csrfmiddlewaretoken: csrfToken,
            storeName: $("#store_name_input").val()
        }
    }).done(function(data){
        if(data["result"] === "failure"){
        console.log(data);
            //TODO implement failure behavior
        }
        window.location.reload();
    });
}

function attachAddItemCallback(){
    $("#add_product").unbind();
    $("#add_product").click(function(){
        $.ajax({
            url: "create/",
            method: "POST",
            data:{
                csrfmiddlewaretoken: csrfToken,
                productName: $("#product_name").val(),
                productQuantity: $("#product_quantity").val(),
                productStoreName:  $("#store_name option:selected").text()
            }
        }).done(function(data){
            if(data["result"] == "failure"){
                //TODO implement failure behavior
                console.log("failed to update record");
            }
            window.location.reload();
        });
    });
}

function attachAddStoreCallback(){
    $("#add_store_button").unbind();
    $("#add_store_button").click(function(){
        addStore();
    });
}

$(document).ready(function(){
    attachCheckCallbacks();
    strikePurchasedProducts();
    attachAddItemCallback();
    attachClearListCallbacks();
    attachSetDefaultStoreCallbacks();
  attachAddStoreCallback();
  attachDeleteCallbacks();
});
