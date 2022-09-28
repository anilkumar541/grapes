from django.urls import path
from mainapp.views import home


urlpatterns = [
    path('', home, name="home"),
]
