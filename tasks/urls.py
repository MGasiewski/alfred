from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>/', views.detail, name='detail'),
    path('<int:task_id>/edit', views.edit, name='edit'),
    path('<int:task_id>/delete', views.delete, name='delete'),
    path('<int:task_id>/complete', views.complete, name='complete')
]

urlpatterns += staticfiles_urlpatterns()
