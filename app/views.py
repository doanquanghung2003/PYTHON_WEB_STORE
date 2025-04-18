from django.shortcuts import render , redirect
from django.http   import HttpResponse,JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as qldn
from .forms import BieuMau_DangKi_ThanhVien

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        # items = [1,2,3,4] #test  
        cartItems = None
    categories = Category.objects.filter(is_sub=False)
    active_category = request.GET.get('category','')
    products = Product.objects.all().values()
    print(products)
    context={'active_category':active_category , 'categories':categories , 'products' : products , 'cartItems' : cartItems}
    return render(request,'app/home.html',context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = [1,2,3,4] #test
        cartItems = order['get_cart_items']
    context={'items' :items,'order': order ,'cartItems' : cartItems}
    return render(request,'app/cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = [1,2,3,4] #test
        cartItems = order['get_cart_items']
    context={'items' :items,'order': order,'cartItems' : cartItems}
    return render(request,'app/checkout.html',context)

def updateItem(request):
    # data = { 'productId': productId, 'action': action }
    data = json.loads(request.body)
    # data = request.POST
    productId = data['productId']
    action = data['action']
    customer = request.user.customer
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer = customer,complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)  
    if action == 'add':
        orderItem.quantity +=1
    elif action == 'remove':
        orderItem.quantity -=1
    orderItem.save()
    if orderItem.quantity <=0:
        orderItem.delete()
    return JsonResponse('added',safe=False)

def register(request):
    # context = {}
    # return render(request,"app/register.html",context)
    if request.method == 'POST':
        ucf = BieuMau_DangKi_ThanhVien(request.POST)
        if ucf.is_valid():
            user = ucf.save()
            qldn(request,user)
            
            return redirect('home')
    else:
        ucf = BieuMau_DangKi_ThanhVien()
        
    return render(request, 'app/register.html' , {'form':ucf})

def login(request):
    context = {}
    return render(request,"app/login.html",context)

def search(request):
    if request.method == "POST":
        searchid = request.POST["searchid"]
        keys = Product.objects.filter(name__contains = searchid)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        # items = [1,2,3,4] #test  
        cartItems = None
    products = Product.objects.all().values()
    return render(request,'app/search.html',{"searchid":searchid,"keys":keys,'products' : products , 'cartItems' : cartItems})

def category(request):
    categories = Category.objects.filter(is_sub =False)
    active_category = request.GET.get('category','')
    if active_category:
        products = Product.objects.filter(category__slug = active_category)
    context={'categories' :categories,'products': products,'active_category' : active_category}
    return render(request,'app/category.html',context)

def detail(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = [1,2,3,4] #test
        cartItems = order['get_cart_items']
    
    id = request.GET.get('id','')
    products = Product.objects.filter(id=id)
    categories = Category.objects.filter(is_sub=False)
    return render(request,'app/detail.html',{'id':id , 'categories':categories , 'products':products , 'items' :items,'order': order ,'cartItems' : cartItems})