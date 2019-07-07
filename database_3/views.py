from django.shortcuts import render, redirect
from .models import Product3



def view_data(request):
    obj = Product3.objects.all()
    db = 3
    return render(request, 'database_3/view data_3.html', {'result': obj, 'db': db})


def save_data(request):
    user = request.user.username
    product = request.POST['product']
    price = request.POST['price']
    quantity = request.POST['quantity']
    obj = Product3(user=user, product=product, price=price, quantity=quantity)
    obj.save()
    return redirect('view_3')




def delete(request, id):
    obj = Product3.objects.get(id=id)
    obj.delete()
    return redirect('view_3')




def update_data(request, id):
    obj = Product3.objects.all()
    single = Product3.objects.get(id=id)
    db = 3
    return render(request, 'database_3/update data_3.html', {'result': obj, 'single': single, 'db': db})


def updated(request, id):
    obj = Product3.objects.get(id=id)
    obj.product = request.POST['product']
    obj.price = request.POST['price']
    obj.quantity = request.POST['quantity']
    obj.save()
    return redirect('view_3')

