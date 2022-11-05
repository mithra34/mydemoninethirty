from django.urls import path
from clothshop import settings
import shopapp
from shopapp import views
from django.conf.urls.static import static
app_name='shopapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('shop/', views.allProdCat, name='allProdCat'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/',views.login,name='login'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),

]