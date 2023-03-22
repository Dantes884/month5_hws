from rest_framework import serializers
from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = 'name products_count'.split()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'


class ProductWithReviews(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = models.Product
        fields = 'name reviews rating'.split()
