from django.urls import path
from apps.shop.views import *


urlpatterns = [
    path("shops/",ShopsView.as_view()),
    path("shop/create/",CreateShopsView.as_view()),
    path("shop/update/<int:pk>/",UpdateShopsView.as_view()),
    path("shop/delete/<int:pk>/",DeleteShopsView.as_view()),
    path("shops/debt_gt/", ShopsDebtGTView.as_view()),

    path("product/create/",CreateProductView.as_view()),
    path("product/delete/<int:pk>/",DeleteProductView.as_view()),
    path("product/update/<int:pk>/",UpdateProductView.as_view()),

    path("message/",QRcodeSendView.as_view()),

]