from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from .models import Category, Product, Review
from .serializers \
    import CategoryValidateSerializer, ProductValidateSerializer, ProductWithReviews, ReviewValidateSerializer


class CategoryListApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryValidateSerializer
    pagination_class = PageNumberPagination


class CategoryDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryValidateSerializer


class ProductListApiView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductValidateSerializer


class ProductDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductValidateSerializer


class ReviewListApiView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewValidateSerializer


class ReviewDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewValidateSerializer


@api_view(['GET'])
def product_with_review_api_view(request):
    products = Product.objects.all()
    serializer = ProductWithReviews(products, many=True)
    return Response(data=serializer.data)
