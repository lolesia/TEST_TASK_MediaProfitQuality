from django.db.models import Sum, Subquery, OuterRef
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import request
from .models import SpendStatistic
from revenue.models import RevenueStatistic


class SpendAggregatedListView(APIView):
    """
    SpendAggregatedListView class defines the API
    endpoints of the SpendStatistic model  summary data
    """

    def get(self, request):

        sort_by_date = SpendStatistic.objects.values('date').distinct().order_by('-date')

        aggregated_data = []

        for item in sort_by_date:
            date = item['date']
            data_for_date = SpendStatistic.objects.filter(date=date).values('name').annotate(
                total_spend=Sum('spend'),
                total_impressions=Sum('impressions'),
                total_clicks=Sum('clicks'),
                total_conversion=Sum('conversion'),
                total_revenue=Sum(Subquery(RevenueStatistic.objects.filter(id=OuterRef("pk")).values("revenue")))
            ).order_by('name')

            aggregated_data.append({
                'date': date,
                'data': data_for_date
            })

        return Response(aggregated_data)

