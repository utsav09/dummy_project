from django.shortcuts import render, redirect
from .models import Product2



def view_data(request):
    obj = Product2.objects.all()
    db = 2
    return render(request, 'database_2/view data_2.html', {'result': obj, 'db': db})


def save_data(request):
    user = request.user.username
    product = request.POST['product']
    price = request.POST['price']
    quantity = request.POST['quantity']
    obj = Product2(user=user, product=product, price=price, quantity=quantity)
    obj.save()
    return redirect('view_2')




def delete(request, id):
    obj = Product2.objects.get(id=id)
    obj.delete()
    return redirect('view_2')




def update_data(request, id):
    obj = Product2.objects.all()
    single = Product2.objects.get(id=id)
    db = 2
    return render(request, 'database_2/update data_2.html', {'result': obj, 'single': single, 'db': db})


def updated(request, id):
    obj = Product2.objects.get(id=id)
    obj.product = request.POST['product']
    obj.price = request.POST['price']
    obj.quantity = request.POST['quantity']
    obj.save()
    return redirect('view_2')

