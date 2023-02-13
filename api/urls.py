from django.urls import path
from .views import item, buy, cancel, success

urlpatterns = [
    path('item/<int:item_id>/', item, name='item'),
    path('buy/<int:item_id>/', buy, name='buy'),
    path('cancel/', cancel, name='cancel'),
    path('success/', success, name='success'),
]