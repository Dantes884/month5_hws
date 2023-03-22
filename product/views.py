from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers


@api_view(['GET'])
def category_list_api_view(request):
    categories = models.Category.objects.all()
    serializer = serializers.CategorySerializer(categories, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category = models.Category.objects.get(id=id)
    except models.Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Category does not exist!'})
    serializer = serializers.CategorySerializer(category)
    return Response(data=serializer.data)


@api_view(['GET'])
def product_list_api_view(request):
    products = models.Product.objects.all()
    serializer = serializers.ProductSerializer(products, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product = models.Product.objects.get(id=id)
    except models.Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Product does not exist!'})
    serializer = serializers.ProductSerializer(product)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_list_api_view(request):
    review = models.Review.objects.all()
    serializer = serializers.ReviewSerializer(review, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = models.Review.objects.get(id=id)
    except models.Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Review does not exist!'})
    serializer = serializers.ReviewSerializer(review)
    return Response(data=serializer.data)


@api_view(['GET'])
def product_with_review_api_view(request):
    products = models.Product.objects.all()
    serializer = serializers.ProductWithReviews(products, many=True)
    return Response(data=serializer.data)
