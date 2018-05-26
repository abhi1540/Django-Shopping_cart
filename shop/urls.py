from django.urls import path
from shop import views


app_name = 'shop'

urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name='product_by_categories'),
    path('<slug:c_slug>/<slug:p_slug>/', views.prodCartDetail, name='prodCartDetail'),

]