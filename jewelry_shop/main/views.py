from django.shortcuts import render, redirect
from .models import Collection ,GetImage


def catalog(request):
  #  if request.method == 'POST':
  #      if 'buy_btn' in request.POST:
   #         deleted_instance = Collection.objects.filter(id=request.POST.get('buy_btn'))
    #        deleted_instance.delete()
    Catalog = Collection.objects.all()
    return render(request, 'main/index.html', {'Catalog': Catalog})

def about(reqest):
    allimages = GetImage.objects.all()
    return render(reqest, 'main/about.html', {'images': allimages})

def list_E(reqest):
    allimages = GetImage.objects.all()
    return render(reqest, 'main/list_E.html')

def display_images(request):
    # getting all the objects of hotel.
    allimages = GetImage.objects.all()
    return render(request, 'show.html', {'images': allimages})