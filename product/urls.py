from django.urls import path
from .views import *

urlpatterns = [
    path('save/', save_or_update_product),
    path('welcome/', welcome_product_page),
    path('edit/<int:pid>', fetch_product_for_edit),
    path('delete/<int:pid>', remove_product_record),
]
