from django.urls import path
from recipes.views import home

# exemplo de apresentação dominio.com/recipes/home, contact, about....
urlpatterns = [
    path('', home),
]
