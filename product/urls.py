from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list_view),
    path('detail/', views.product_detail_view),
    path("detail/home/", views.home),
]


