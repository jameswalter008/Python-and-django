from django.shortcuts import render,redirect
from django.http import HttpResponse
from accounts.models import *
from accounts.form import *
from django.forms import inlineformset_factory

# Create your views here.
def customers(request,id):
    customers=Customer.objects.get(id=id)
    orders=customers.order_set.all()
    order_count=orders.count()
    # return HttpResponse(id)
    return render(request,'accounts/customers.html',{
        'customers':customers,
        'orders':orders,
        'order_counts':order_count
    })

def product(request):
    products=Product.objects.all()
    return render(request,'accounts/products.html',{
        'products':products
    })


def dashboard(request):
    customers=Customer.objects.all()
    orders=Order.objects.all()
    total=orders.count()
    delivered=Order.objects.filter(status="delivered").count()
    pending=Order.objects.filter(status="pending").count()
    return render(request,'accounts/dashboard.html',{
        'customers':customers,
        'orders':orders,
        'total':total,
        'delivered':delivered,
        'pending':pending
    })

def ordercreate(request,customerID):
    OrderFormSet=inlineformset_factory(Customer,Order,fields=('product','status'),extra=10)
    customer=Customer.objects.get(id=customerID)
    formset=OrderFormSet(instance=customer,queryset=Order.objects.none())
    if request.method=="POST":

        formset=OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save();
            return redirect('/');
            
    return render(request,'accounts/order_form.html',
    {   
        'formset':formset
    })

def orderupdate(request,orderID):
    order=Order.objects.get(id=orderID);
    form=OrderForm(instance=order)
    if request.method=="POST":

        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save();
            return redirect('/');
            
    return render(request,'accounts/order_form.html',
    {   
        'form':form
    }
    )

def orderdelete(request,orderID):
    order=Order.objects.get(id=orderID);
    if request.method=="POST":
        order.delete();
        return redirect('/')
    order=Order.objects.get(id=orderID);
    return render(request,'accounts/orderdelete.html',
    {
        'order':order
    }
    )