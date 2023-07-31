from django.shortcuts import render

# Create your views here.
def condition (request):
    d={'name':'lohidasu'}
    return render(request,'condition.html',context=d)
def datarender(request):
    return render(request,'datarender.html')