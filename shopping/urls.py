from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'shopping'
urlpatterns = [
    path('', views.index, name='index'),
    path('purchase/<int:product_id>/', views.purchase, name='purchase'),
    path('delete/<int:product_id>/', views.delete_product, name='delete'),
    path('create/', views.create, name='create'),
    path('clear_list/<int:store_id>/', views.clear_list, name="clear-list"),
    path('create_store/', views.create_store, name='create-store'),
    path('edit/<int:product_id>/<str:product_name>/<int:product_quantity>/<str:product_store>/', views.edit_product, name='edit-product'),
]

urlpatterns += staticfiles_urlpatterns()
