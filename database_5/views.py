from django.shortcuts import render, redirect
from .models import Product5



def view_data(request):
    obj = Product5.objects.all()
    db = 5
    return render(request, 'database_5/view data_5.html', {'result': obj, 'db': db})


def save_data(request):
    user = request.user.username
    product = request.POST['product']
    price = request.POST['price']
    quantity = request.POST['quantity']
    obj = Product5(user=user, product=product, price=price, quantity=quantity)
    obj.save()
    return redirect('view_5')




def delete(request, id):
    obj = Product5.objects.get(id=id)
    obj.delete()
    return redirect('view_5')




def update_data(request, id):
    obj = Product5.objects.all()
    single = Product5.objects.get(id=id)
    db = 5
    return render(request, 'database_5/update data_5.html', {'result': obj, 'single': single, 'db': db})


def updated(request, id):
    obj = Product5.objects.get(id=id)
    obj.product = request.POST['product']
    obj.price = request.POST['price']
    obj.quantity = request.POST['quantity']
    obj.save()
    return redirect('view_5')

