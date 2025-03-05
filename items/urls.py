from django.urls import path

from .views import ItemListView, VoteView

urlpatterns = [
    path("", ItemListView.as_view(), name="index"),
    path("<int:pk>/", VoteView.as_view(), name="vote"),
]