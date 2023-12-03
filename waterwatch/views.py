import pandas as pd
from django.core.serializers import serialize
from django.shortcuts import render
from django.http import HttpResponse

from waterwatch.models import WaterConsumption


def home(request):
    """Renders home page"""
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home page'
        }
    )


def waterconsumption_dataset(request):
    waterconsumption = serialize('geojson', WaterConsumption.objects.all())
    return HttpResponse(waterconsumption, content_type='json')


def top10_consumers(request):
    df_top10 = pd.DataFrame.from_records(WaterConsumption.objects.all().values())
    df_top10_x_y_sorted = df_top10.sort_values(['AvgMonthlyKL'], ascending=False)
    df_top10_x_y = df_top10_x_y_sorted[['Suburb', 'AvgMonthlyKL']]
    df_top10_rows = df_top10_x_y.head(10)
    df_top10_rows_json = df_top10_rows.to_json(orient='records')

    return HttpResponse(df_top10_rows_json, content_type='json')
