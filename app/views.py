from django.shortcuts import render

# Create your views here.

def usdfilters(request):
    d={'data':'Hai hOW aRE yoU'}
    return render(request,'usdfilters.html',d)