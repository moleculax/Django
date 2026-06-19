
#apps/categories/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.categories, name='categories_index'),                # todas
    path('<int:category_id>/', views.categories, name='category_detail')  # por id
]
