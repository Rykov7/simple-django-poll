from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, RedirectView

from items.models import Item, Vote


def get_ip_and_ua(request):
    return request.META.get("REMOTE_ADDR", "0.0.0.0"), request.META.get("HTTP_USER_AGENT", "Unknown")


class ItemListView(ListView):
    model = Item
    context_object_name = "item_list"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        ip, user_agent = get_ip_and_ua(self.request)
        context['ip'] = ip
        context['choice'] = Vote.objects.filter(ip=ip, user_agent=user_agent).first()
        return context


class VoteView(RedirectView):
    pattern_name  = "index"

    def get_redirect_url(self, *args, **kwargs):
        ip, user_agent = get_ip_and_ua(self.request)
        item = get_object_or_404(Item, pk=kwargs["pk"])
        Vote.objects.update_or_create(ip=ip, user_agent=user_agent, defaults={'choice_id': item.pk})
        return reverse(self.pattern_name)
