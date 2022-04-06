from django.urls import path

from recipes.views import home, sobre, contato

urlpatterns = [
    path('', home),
    path('home/', home),
    path('contato/', contato),
    path('sobre/', sobre),
]
