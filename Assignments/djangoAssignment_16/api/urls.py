from django.urls import path
from api.views import ItemDetail, item_list

urlpatterns = [
    path('', item_list, name='item_list'),
    path('<int:pk>/', ItemDetail.as_view(), name='item_detail'),
]