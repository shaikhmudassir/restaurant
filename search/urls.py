from django.urls import path
from .views import SearchDishes
urlpatterns = [
    path('', SearchDishes.as_view(), name="search"),
]
