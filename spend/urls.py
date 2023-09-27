from django.urls import path
from .views import SpendAggregatedListView


urlpatterns = [
    path('', SpendAggregatedListView.as_view())
]
