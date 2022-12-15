from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Collection ,GetImage,Order,User,MethodDeliveryTable
import sqlite3

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

def create(request,correct_id):
    correct_product = Collection.objects.all()[correct_id - 1]
    """    error = ''
    if request.method == 'POST':
        form = OrderForm(request.POST)
        form1 = UserForm(request.POST)
        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
            return redirect('catalog')
        else:
            error = "Неверно заполнена форма"
    orderfilds = OrderForm()
    Userfilds = UserForm()"""


    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            #fullname = fullname_share(form.cleaned_data.get('Name'))

            method_dlivery = form.cleaned_data.get('method_delivery')
            adress = form.cleaned_data.get('adress')
            name = form.cleaned_data.get('name')
            surname = form.cleaned_data.get('surname')


            if 'createb' in request.POST:
                print(adress)
                sqlite_connection = sqlite3.connect('mybd.sqlite3')
                cursor = sqlite_connection.cursor()


                sqlite_select_query = f"insert into [order](method_delivery,product,price_order,address,user_name,user_surname) " \
                                      f"values ({method_dlivery}, {correct_id},{str(correct_product.price)},'{str(adress)}','{str(name)}','{str(surname)}')"
                print(sqlite_select_query)
                cursor.execute(sqlite_select_query)
                sqlite_connection.commit()

                cursor.close()


            return redirect('/')

    else:
        form = OrderForm()




    return render(request, 'main/order.html',{'form':form,'product':correct_product})

def order(reqest,correct_id):
    zak = User.objects.all()
    correct_product = Collection.objects.all()[correct_id - 1]
    delivery = MethodDeliveryTable.objects.all()

    print(delivery)


    return render(reqest, 'main/order.html',{'correct_product': correct_product})