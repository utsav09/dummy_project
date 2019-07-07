from django.shortcuts import render
from database_1.models import Product1
from database_2.models import Product2
from database_3.models import Product3
from database_4.models import Product4
from database_5.models import Product5


def view(request):
    obj1 = Product1.objects.all()
    obj2 = Product2.objects.all()
    obj3 = Product3.objects.all()
    obj4 = Product4.objects.all()
    obj5 = Product5.objects.all()
    return render(request, 'database/All Data.html', {'obj1': obj1,
                  'obj2': obj2, 'obj3': obj3, 'obj4': obj4, 'obj5': obj5})
