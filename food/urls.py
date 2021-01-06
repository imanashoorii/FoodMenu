from . import views
from django.urls import path

app_name = 'food'

urlpatterns = [
    path('', views.index, name='home'),
    path('delete_item/<int:product_id>/', views.delete_item, name='delete'),
    path('detail/<int:product_id>/', views.detail_view, name='detail'),
    path('add/', views.add_product, name='add-product'),
    path('update/<int:product_id>', views.update_product, name='update-product'),
]