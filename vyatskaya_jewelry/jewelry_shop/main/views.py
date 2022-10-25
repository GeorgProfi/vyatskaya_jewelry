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

def detail(reqest, product_id ):
    Catalog = Collection.objects.all()[product_id - 1]
    product = Catalog
    print(product.chapter.chapter)
    return render(reqest, 'main/detal_of_product.html', {'product': product})

def display_images(request):
    # getting all the objects of hotel.
    allimages = GetImage.objects.all()
    return render(request, 'show.html', {'images': allimages})