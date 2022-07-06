from django.urls import path,include
from . import views
app_name='ecommerceapp'
urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),
    path('<slug:C_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:p_slug>/',views.productDetails,name='prodCatdetail'),
]