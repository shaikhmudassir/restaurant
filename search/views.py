from django.shortcuts import render
from django.views import View
from .models import Restaurant, Dishes

class SearchDishes(View):
    def get(self, request):
        query = request.GET.get('search')
        print(query)
        if query:
            results = Dishes.objects.filter(item__icontains=query)
            return render(request, "search/index.html", {'results': results})
        return render(request, "search/index.html", {'results': None})
    