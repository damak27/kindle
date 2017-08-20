from django.shortcuts import render,redirect
from .models import Events,Order
from .forms import OrderForm
from django.contrib import messages

# Create your views here.
def homeview(request):
    queryset = Events.objects.all()

    form=OrderForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Thank you !!Order has been recieve")
        return redirect('kindlebizy:Homepage')
    content={"form":form,
             "events":queryset}
    return render(request,"kindlebizy/homepage.html",content)

def popview(request):
    content=""
    return render(request,"kindlebizy/about.html",{'content':content})

def order(request):
    queryset = Events.objects.all()

    form=OrderForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Thank you !!Order has been recieve")
        return redirect('kindlebizy:Homepage')
    content={"form":form,
             "events":queryset}
    return render(request,"kindlebizy/order.html",content)
