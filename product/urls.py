from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/categories/', views.CategoryListApiView.as_view()),
    path('api/v1/categories/<int:pk>/', views.CategoryDetailApiView.as_view()),
    path('api/v1/products/', views.ProductListApiView.as_view()),
    path('api/v1/products/<int:pk>/', views.ProductDetailApiView.as_view()),
    path('api/v1/review/', views.ReviewListApiView.as_view()),
    path('api/v1/review/<int:pk>/', views.ReviewDetailApiView.as_view()),
    path('api/v1/products/reviews/', views.product_with_review_api_view),
]
