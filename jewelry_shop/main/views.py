from django.shortcuts import render, redirect
from .models import Collection


def catalog(request):
    if request.method == 'POST':
        if 'buy_btn' in request.POST:
            deleted_instance = Collection.objects.filter(id=request.POST.get('buy_btn'))
            deleted_instance.delete()
    Catalog = Collection.objects.all()
    return render(request, 'main/index.html', {'Catalog': Catalog})

def about(reqest):
    return render(reqest, 'main/about.html')