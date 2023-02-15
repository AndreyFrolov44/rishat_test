from django.urls import path
from .views import item, buy, cancel, success

urlpatterns = [
    path('item/<int:order_id>/', item, name='item'),
    path('buy/<int:order_id>/', buy, name='buy'),
    path('cancel/', cancel, name='cancel'),
    path('success/', success, name='success'),
]