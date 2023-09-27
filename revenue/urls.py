from django.urls import path
from .views import RevenueAggregatedListView

urlpatterns = [
    path('', RevenueAggregatedListView.as_view())
]
