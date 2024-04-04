from django.urls import path
from recipes.views import home, contact, about

# exemplo de apresentação dominio.com/recipes/home, contact, about....
urlpatterns = [path('', home),  # /home/
               path('contact/', contact),  # /contact/
               path('about/', about)  # /about/
               ]
