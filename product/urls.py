from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/categories/', views.category_list_api_view),
    path('api/v1/categories/<int:id>/', views.category_detail_api_view),
    path('api/v1/products/', views.product_list_api_view),
    path('api/v1/products/<int:id>/', views.product_detail_api_view),
    path('api/v1/review/', views.review_list_api_view),
    path('api/v1/review/<int:id>/', views.review_detail_api_view),
    path('api/v1/products/reviews/', views.product_with_review_api_view),
]
