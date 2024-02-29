from django import template

from liberty_market.models import ItemLike

register = template.Library()


def check_like(item, user):
    return ItemLike.objects.filter(item=item, author=user).exists()


register.filter(check_like)
