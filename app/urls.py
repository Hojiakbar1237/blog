from django.urls import path
from .views import home,about,portfolio

urlpatterns = [
    path("",home),
    path("about/",about),
    path("portfolio/",portfolio)

]