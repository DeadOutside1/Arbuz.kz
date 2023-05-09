from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .disable import unauthenticated_user

from .models import *


@login_required(login_url='login')
def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)


def adminPage(request):
    cus = Customer.objects.all()
    contex = {'cus': cus}
    return render(request, 'store/admin.html', contex)


def add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        cus = Customer(
            name=name,
            email=email,
            address=address,
            phone=phone
        )
        cus.save()
        return redirect('adminPage')

    return render(request, 'store/admin.html')


def edit(request):
    cus = Customer.objects.all()
    context = {
        'cus': cus,
    }
    return redirect(request, 'store/admin.html', context)


def update(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        cus = Customer(
            id=id,
            name=name,
            email=email,
            address=address,
            phone=phone
        )
        cus.save()
        return redirect('adminPage')
    return redirect(request, 'store/admin.html')


def delete(request, id):
    cus = Customer.objects.filter(id=id)
    cus.delete()
    contex = {
        'cus': cus,
    }
    return redirect('adminPage')


@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            username = request.user.username
            messages.success(request, f'{username},Your profile is update.')
            return redirect('/')
    else:
        form = ProfileForm(instance=request.user.profile)
    contex = {'form': form}
    return render(request, 'store/profile.html', contex)


@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f'{username},You are logged in.')
            return redirect("store")
        else:
            messages.info(request, 'Wrong username or password')
            return redirect('login')

    return render(request, 'store/login_page.html')


@unauthenticated_user
def register_user(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Account is create.')
            return redirect('login')
        else:
            context = {'form': form}
            messages.info(request, 'Invalid Invalid')
            return render(request, 'store/register_page.html', context)
    context = {'form': form}
    return render(request, 'store/register_page.html', context)


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.info(request, 'You  logged out successfully')
    return render(request, 'store/login_page.html')
