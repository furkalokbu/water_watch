from django.contrib import admin
from django.urls import path, re_path

from waterwatch.views import home, waterconsumption_dataset, top10_consumers

urlpatterns = [
    path('waterconsumption/', waterconsumption_dataset, name='waterconsumption'),
    path('top10_consumers', top10_consumers, name='top10consumers'),
    path('', home, name='home'),
    path('admin/', admin.site.urls),
]
