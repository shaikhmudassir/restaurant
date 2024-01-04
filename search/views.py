from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Restaurant, Dishes
import json

class SearchDishesView(View):
    def get(self, request):
        query = request.GET.get('search')
        if query:
            results = Dishes.objects.filter(item__icontains=query)
            return render(request, "search/index.html", {'results': results})
        return render(request, "search/index.html", {'results': None})

class DetailView(View):
    def get(self, request, id):
        result = Restaurant.objects.get(ID=id)
        print(result.other_details[0])

        return render(request, "search/detail.html", {'result': json.loads(result.other_details)})