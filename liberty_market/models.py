from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE

from liberty_market.uitls import avatar_path, item_photos


class AbstractBaseModel(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(AbstractUser):
    image = models.ImageField(upload_to=avatar_path, default='avatar.jpg')
    author_like = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Category(AbstractBaseModel):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    price = models.IntegerField()
    category = models.ForeignKey(Category, CASCADE, related_name='category')
    royalties = models.IntegerField()
    image = models.FileField(upload_to=item_photos)
    owner_full_name = models.CharField(max_length=128)
    owner_user_name = models.CharField(max_length=128)
    ends_in = models.DateTimeField()

    def __str__(self):
        return self.title


class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='order')

    def __str__(self):
        return self.item.title


class ItemLike(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='like')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.item}--{self.author}'
