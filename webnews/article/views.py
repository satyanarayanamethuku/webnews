from django.shortcuts import render
from .models import Aritcle
from django.http import HttpResponse

# Create your views here.

def greet(request):
     return HttpResponse("<h1>Hello Pnv</h1>")



def display_view(request):
    all=Aritcle.objects.all()
    return render(request,'frontpage.html',{'all':all})
    
    
    # object=Aritcle.objects.all()
    # if object:
    # context={
    #     'all_article':[object]
    # }

    # return render(request,'frontpage.html',context)





