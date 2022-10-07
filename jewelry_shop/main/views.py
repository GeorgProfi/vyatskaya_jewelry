from django.shortcuts import render

# Create your views here.
def catalog(request):
    return render(request,'main/index.html')

def about(reqest):
    return render(reqest, 'main/about.html')