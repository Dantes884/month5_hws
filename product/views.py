from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers


@api_view(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        categories = models.Category.objects.all()
        serializer = serializers.CategorySerializer(categories, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = serializers.CategoryValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        name = serializer.validated_data.get('name')
        category = models.Category.objects.create(name=name)
        return Response(data=serializers.CategorySerializer(category).data)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, id):
    try:
        category = models.Category.objects.get(id=id)
    except models.Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Category does not exist!'})
    if request.method == 'GET':
        serializer = serializers.CategorySerializer(category)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category.name = serializer.validated_data.get('name')
        return Response(data=serializers.CategorySerializer(category).data)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        products = models.Product.objects.all()
        serializer = serializers.ProductSerializer(products, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = serializers.ProductValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        name = serializer.validated_data.get('name')
        price = serializer.validated_data.get('price')
        description = serializer.validated_data.get('description')
        category = serializer.validated_data.get('category')
        product = models.Product.objects.create(name=name, price=price, description=description)
        product.category.set(category)
        product.save()
        return Response(data=serializers.ProductSerializer(product).data)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        product = models.Product.objects.get(id=id)
    except models.Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Product does not exist!'})
    if request.method == 'GET':
        serializer = serializers.ProductSerializer(product)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.ProductValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product.name = serializer.validated_data.get('name')
        product.description = serializer.validated_data.get('description')
        product.price = serializer.validated_data.get('price')
        category = serializer.validated_data.get('category')
        product.category.set(category)
        product.save()
        return Response(data=serializers.ProductSerializer(product).data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        review = models.Review.objects.all()
        serializer = serializers.ReviewSerializer(review, many=True)
        return Response(data=serializer.data)
    if request.method == 'POST':
        serializer = serializers.ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        text = serializer.validated_data.get('text')
        stars = serializer.validated_data.get('stars')
        product_id = serializer.validated_data.get('product_id')
        review = models.Review.objects.create(text=text, stars=stars, product_id=product_id)
        return Response(data=serializers.ReviewSerializer(review).data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = models.Review.objects.get(id=id)
    except models.Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Review does not exist!'})
    if request.method == 'GET':
        serializer = serializers.ReviewSerializer(review)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review.text = serializer.validated_data.get('text')
        review.stars = serializer.validated_data.get('stars')
        review.product_id = serializer.validated_data.get('product_id')
        return Response(data=serializers.ReviewSerializer(review).data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def product_with_review_api_view(request):
    products = models.Product.objects.all()
    serializer = serializers.ProductWithReviews(products, many=True)
    return Response(data=serializer.data)
