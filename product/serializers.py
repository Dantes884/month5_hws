from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Product, Category, Review, Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'name products_count'.split()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'name price description category_name'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars product_name'.split()


class ProductWithReviews(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = 'name reviews rating'.split()


class ProductValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField()
    price = serializers.IntegerField(min_value=1)
    category = serializers.ListField(child=serializers.IntegerField())
    tag = serializers.ListField(child=serializers.IntegerField(), required=False)

    def validate_categories(self, categories):
        for i in categories:
            try:
                Category.objects.get(id=i)
            except Category.DoesNotExist:
                raise ValidationError(f'Genre with id ({i}) not found')
            return i


    def validate_tags(self, tag):
        filtered_tags = Tag.objects.filter(id__in=tag)
        if len(tag) == filtered_tags.count():
            return tag

        lst_ = {i['id'] for i in filtered_tags.values_list().values()}

        raise ValidationError(f'This ids doesnt exist {set(tag).difference(lst_)}')


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField()


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    stars = serializers.IntegerField(min_value=1, max_value=5)
    product_id = serializers.IntegerField()

    def validate_product_id(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError(f'Director with id ({product_id}) not found')
        return product_id
