from django.shortcuts import get_object_or_404
from django.views.generic import ListView, RedirectView

from items.models import Item


class ItemListView(ListView):
    model = Item
    context_object_name = "item_list"


class VoteView(RedirectView):
    url = '/'

    def get_redirect_url(self, *args, **kwargs):
        item = get_object_or_404(Item, pk=kwargs["pk"])
        item.counter += 1
        item.save()
        return super().get_redirect_url(*args, **kwargs)