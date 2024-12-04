from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path("",views.home,name="home"),
    path("<uuid:uuid>",views.product_detail,name="product_detail"),
    path("search",views.search ,name="search"),
]
