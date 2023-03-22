from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @property
    def products_count(self):
        return self.products.count()


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ManyToManyField(Category, blank=True, related_name='products')

    def __str__(self):
        return self.name

    @property
    def rating(self):
        stars = [review.stars for review in self.reviews.all()]
        return round(sum(stars) / len(stars), 2)


class Review(models.Model):
    STARS = ((i, '*' * i) for i in range(1, 6))
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(choices=STARS, null=True)

    def __str__(self):
        return self.text
