from django.urls import path
from .views import SearchDishesView, DetailView

app_name = 'search'

urlpatterns = [
    path('', SearchDishesView.as_view(), name="search"),
    path('restaurant/<str:id>', DetailView.as_view(), name="detail"),
]
