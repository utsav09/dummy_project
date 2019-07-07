from django.shortcuts import render, redirect
from .models import Product1



def view_data(request):
    obj = Product1.objects.all()
    db = 1
    return render(request, 'database_1/view data_1.html', {'result': obj, 'db': db})


def save_data(request):
    user = request.user.username
    product = request.POST['product']
    price = request.POST['price']
    quantity = request.POST['quantity']
    obj = Product1(user=user, product=product, price=price, quantity=quantity)
    obj.save()
    return redirect('view_1')




def delete(request, id):
    obj = Product1.objects.get(id=id)
    obj.delete()
    return redirect('view_1')




def update_data(request, id):
    obj = Product1.objects.all()
    single = Product1.objects.get(id=id)
    db = 1
    return render(request, 'database_1/update data_1.html', {'result': obj, 'single': single, 'db': db})


def updated(request, id):
    obj = Product1.objects.get(id=id)
    obj.product = request.POST['product']
    obj.price = request.POST['price']
    obj.quantity = request.POST['quantity']
    obj.save()
    return redirect('view_1')

