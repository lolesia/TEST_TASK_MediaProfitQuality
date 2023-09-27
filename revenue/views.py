from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import request
from .models import RevenueStatistic


class RevenueAggregatedListView(APIView):
    """
    RevenueAggregatedListView class defines the API
    endpoints of the SpendStatistic model  summary data
    """

    def get(self, request):
        sort_by_date = RevenueStatistic.objects.values('date').distinct().order_by('-date')

        aggregated_data = []

        for item in sort_by_date:
            date = item['date']
            data_for_date = RevenueStatistic.objects.filter(date=date).values('name').annotate(
                total_revenue=Sum('revenue'),
                total_spend=Sum('spend__spend'),
                total_impressions=Sum('spend__impressions'),
                total_clicks=Sum('spend__clicks'),
                total_conversion=Sum('spend__conversion')
            ).order_by('name')

            aggregated_data.append({
                'date': date,
                'data': data_for_date
            })
        return Response(aggregated_data)



