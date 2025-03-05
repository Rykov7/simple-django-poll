from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, RedirectView

from items.models import Item, Vote


class ItemListView(ListView):
    model = Item
    context_object_name = "item_list"


class VoteView(RedirectView):
    pattern_name  = "index"

    def get_redirect_url(self, *args, **kwargs):
        ip = self.request.META.get("REMOTE_ADDR")
        item = get_object_or_404(Item, pk=kwargs["pk"])
        Vote.objects.update_or_create(ip=ip, defaults={'choice_id': item.pk})
        return reverse(self.pattern_name)
