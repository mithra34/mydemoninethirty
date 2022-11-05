from django.urls import path
from clothshop import settings
from django.conf.urls.static import static
from cartapp import views
app_name='cartapp'
urlpatterns = [

    path('cartapp/add/<int:product_id>/',views.add_cart,name="add_cart"),
    path(' ', views.cart_detail, name="cart_detail"),

    path('cartapp/remove/<int:product_id>/', views.cart_remove, name="cart_remove"),
    path('cartapp/remove_all/<int:product_id>/', views.remove_all, name="remove_all")
   ]