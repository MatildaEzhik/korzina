from django.urls import path

from cart import views

urlpatterns = [
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('summary/', views.cart_summary, name='cart_summary'),
]
