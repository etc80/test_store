from django.shortcuts import render, redirect
from store.forms import UserForm, ProductForm
from django.contrib.auth.models import User
from store.models import Product, Favorites
from django.contrib.auth import authenticate, login as native_login, logout as native_logout
from django.contrib.messages import debug, info, warning, error, success
from django.db import IntegrityError


# Create your views here.
def home(request):
    data = {}
    #data['products'] = Product.objects.all()
    data['categories'] = Product.CATEGORIES
    # data['sessionID'] = request.COOKIES['sessionid']
    # request.COOKIES['items'] = ['testitemID']
    # request.COOKIES['items'].extend(['testitemID2'])
    # data['mycookies'] = request.COOKIES['items']
    return render(request, 'store/home.html', data)


def register(request):
    data = {}
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                user = User(username=form.data['username'])
                user.set_password(form.data['password'])
                if User.objects.all().count() == 0:
                    user.is_superuser = True
                user.save()
                native_login(request, user)
                return redirect('home')
            except IntegrityError:
                error(request, 'Username is not unique')
    data['form'] = form
    return render(request, 'store/register.html', data)


def login(request):
    data = {}
    form = UserForm()
    if request.method == "POST":
        #form = UserForm(request.POST)
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is None:
            error(request, 'Invalid user name or password')
            return redirect('login')
        else:
            native_login(request, user)
            return redirect('home')
    data['form'] = form
    return render(request, 'store/login.html', data)


def logout(request):
    native_logout(request)
    return redirect('home')


def favorites(request):
    data = {}
    favors = Favorites.objects.filter(user=request.user.pk)
    fav_prods = []
    for item in favors:
        fav_prods.append(item.product)
    data['products'] = fav_prods
    return render(request, 'store/favorites.html', data)


def like(request, url):
    data = {}
    product_pk = request.GET.get('pk', None)
    if not product_pk:
        return redirect(url)
    try:
        liked = Favorites.objects.get(user=request.user.pk, product=product_pk)
        liked.delete()
    except:
        cur_product = Product.objects.get(pk=product_pk)
        cur_user = User.objects.get(pk=request.user.pk)
        like = Favorites(user=cur_user, product=cur_product)
        like.save()
    return redirect(url)


def createproduct(request):
    data = {}
    if request.method != "POST":
        form = ProductForm()
        data['form'] = form
        return render(request, 'store/createproduct.html', data)
    form = ProductForm(request.POST, request.FILES)
    data['form'] = form
    if form.is_valid():
        try:
            pr = Product(**form.cleaned_data)
            pr.save()
            return redirect('createproduct')
        except Exception:
            warning(request, 'Product was not created due to some issue')
            return render(request, 'store/createproduct.html', data)


def productlist(request, category, producer):
    data = {}
    data['category'] = ''
    data['subcategory'] = ''
    categories = Product.CATEGORIES
    for cat in categories:
        if cat[0] == category:
            data['category'] = cat[0]
        for c in cat[1]:
            if c[0] == category:
                data['subcategory'] = category
                data['subcatname'] = c[1]
                break
    startprice = request.GET.get('pr1')
    endprice = request.GET.get('pr2')
    if data['subcategory']:
        data['products'] = Product.objects.filter(category=category)
    else:
        cats = Product.get_cats_by_group(category, Product.CATEGORIES)
        data['products'] = Product.objects.filter(category__in=cats)
    if producer:
        data['products'] = data['products'].filter(producer=producer)
    if startprice:
        data['products'] = data['products'].filter(price__gt=startprice)
    if endprice:
        data['products'] = data['products'].filter(price__lt=endprice)
    data['categories'] = categories
    data['producers'] = Product.PRODUCERS
    return render(request, 'store/productlist.html', data)


def productview(request, pk):
    data = {}
    data['product'] = Product.objects.get(pk=pk)
    data['producer'] = data['product'].get_producer_display()
    try:
        Favorites.objects.get(user=request.user.pk, product=data['product'].pk)
        data['liked'] = 'Unlike'
    except:
        data['liked'] = 'Like'
    return render(request, 'store/productview.html', data)
