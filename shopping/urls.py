from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'shopping'
urlpatterns = [
    path('', views.index, name='index'),
    path('complete/<int:product_id>/', views.delete, name='complete'),
    path('purchase/<int:product_id>/', views.purchase, name='purchase'),
    path('create/', views.create, name='create'),
    path('create_store/', views.create_store, name='create-store')
]

urlpatterns += staticfiles_urlpatterns()
