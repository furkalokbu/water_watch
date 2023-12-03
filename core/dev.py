from .base import *


ALLOWED_HOSTS: list[str] = env('ALLOWED_HOSTS')

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'HOST': env('DB_HOST'),
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
    }
}

SERIALIZATION_MODULES = {
    'geojson': 'djgeojson.serializers'
}

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (-33.925 ,18.625),
    'DEFAULT_ZOOM': 10,
    'MAX_ZOOM': 20,
    'MIN_ZOOM': 3,
    'SCALE':'both',
    'ATTRIBUTION_PREFIX':'Powered by EBISYS',
    'TILES': [('Open Street Map', 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {'attribution': '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>', 'maxZoom': 20}),
          ('Terrain Map', 'http://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {'attribution': 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community', 'maxZoom': 20}),
          ('Data Map', 'https://cartodb-basemaps-{s}.global.ssl.fastly.net/dark_all/{z}/{x}/{y}.png', {'attribution':'&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="http://cartodb.com/attributions">CartoDB</a>', 'maxZoom': 20})],
    'OVERLAYS': [('Suburbs', 'https://citymaps.capetown.gov.za/agsext1/rest/services/Theme_Based/EGISViewer/MapServer/76/query?outFields=*&where=1%3D1', {'attribution': '&copy; IGN'}),
                 ('Dams', 'http://server/a/{z}/{x}/{y}.png', {'attribution': '&copy; IGN'})]

}