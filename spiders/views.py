from django.shortcuts import render
from .models import Spider
from django.shortcuts import get_object_or_404

def home(request):
    context = {
        'spiders': Spider.objects.all()
    }
    return render(request, 'spiders/home.html', context)

def specie(request, spider_id):
    spider_type = get_object_or_404(Spider, pk=spider_id)
    return render(request, 'spiders/spider.html', {'spider':spider_type})
