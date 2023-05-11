from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponse
from .models import smsmodel

from .serializer import smsserializer
# Create your views here.
class smsAPI(ModelViewSet):
    queryset = smsmodel.objects.all()
    serializer_class = smsserializer
def create(request):
    if request.method == 'POST':
        name= request.POST['name']
        RAM = request.POST['RAM']
        price = request.POST['price']
        location = request.POST['location']

        item = smsmodel(name=name,RAM=RAM,price=price,location=location)
        item.save()
        return HttpResponse("Saved Succesfully")
    elif request.method == 'GET':
        return render(request,'index.html')
def readone(request):
    if request.method == 'POST':
        id = request.POST['id']
        item=smsmodel.objects.get(id=id)

        return render(request,'readone.html',{'item':item})

    elif request.method == 'GET':
        return render(request,'readone.html')


def readall(request):
    item = smsmodel.objects.all()

    return render(request,'readall.html',{'item':item})

def delete(request):
    id = request.POST['id']
    item = smsmodel.objects.get(id=id)
    smsmodel.delete(item)
    return render(request,'readall.html')

def update(request):
    if request.method == 'POST':
        id = request.POST.get('id')

        name = request.POST.get('name')
        RAM = request.POST.get('RAM')
        price = request.POST.get('price')
        location = request.POST.get('location')

        item= smsmodel(id=id, name=name, RAM=RAM, price=price, location=location)
        item.save()

        return HttpResponse('updated successfully')
    elif request.method =='GET':
        id=request.GET.get('id')
        items = smsmodel.objects.get(id=id)
        return render(request, 'updatepage.html',{'items': items})
