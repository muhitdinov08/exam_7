from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View

from liberty_market.form import CreateItemForm, UserRegistrationForm, LoginForm, ItemUpdateForm
from liberty_market.models import Item, Author, Order, ItemLike


class Home_page(View):
    def get(self, request):
        items = Item.objects.all()
        size = request.GET.get("size", 4)
        page = request.GET.get("page", 1)
        paginator = Paginator(items, size)
        page_obj = paginator.page(page)
        return render(request, 'liberty_market/index.html',
                      {"page_obj": page_obj, "num_pages": paginator.num_pages, 'items': items})


class Explore_page(View):
    def get(self, request):
        top_items = Item.objects.all().order_by('ends_in')[:4]

        items = Item.objects.all()

        return render(request, 'liberty_market/explore.html', {'items': items, 'top_items': top_items})


class Filter_category(View):
    def get(self, request, category_id):
        items = Item.objects.filter(category=category_id)
        return render(request, 'liberty_market/explore.html', {'items': items})


class Item_detail(View):
    def get(self, request, pk):
        item = Item.objects.get(pk=pk)

        return render(request, 'liberty_market/details.html', {'item': item})


class Author_page(View):
    def get(self, request):
        authors = Author.objects.all()
        return render(request, 'liberty_market/author.html', {"authors": authors})


class CreateItem(View):
    def get(self, request):
        form = CreateItemForm(data=request.GET, files=request.FILES)
        return render(request, 'liberty_market/create.html', {'form': form})

    def post(self, request):
        form = CreateItemForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully created')
            return redirect('liberty_market:home_page')
        else:
            return render(request, 'liberty_market/create.html', {'form': form})


class UserLoginView(View):
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Author successfully logged in')
                return redirect('liberty_market:home_page')
            else:
                messages.warning(request, 'Author not found')
        else:
            return render(request, 'liberty_market/login.html', {'form': form})

    def get(self, request, **kwargs):
        form = LoginForm()
        return render(request, 'liberty_market/login.html', {'form': form})


class UserRegisterView(View):
    def post(self, request):
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Author successfully registered')
            return redirect('liberty_market:login')
        else:
            return render(request, 'liberty_market/register.html', {'form': form})

    def get(self, request, **kwargs):
        form = UserRegistrationForm(data=request.GET)
        return render(request, 'liberty_market/register.html', {'from': form})


class UserLogoutView(View):
    def get(self, request, *kwargs):
        logout(request)
        messages.success(request, f'{request.user.username} successfully logged')
        return redirect('liberty_market:home_page')


class Filter_items_category(View):
    def get(self, request, category_id):
        items = Item.objects.filter(category=category_id, author=request.user)
        return render(request, 'liberty_market/my_items.html', {'items': items})


class OrdersView(View):
    def get(self, request, id):
        Order.objects.create(item_id=id)
        messages.success(request, 'Order successfully added')
        return redirect('liberty_market:item_details')


class MyItems(View):
    def get(self, reqeust):
        items = Item.objects.filter(author__username=reqeust.user.username)
        return render(reqeust, 'liberty_market/my_items.html', {'items': items})


class UpdateItem(View):
    def get(self, request, item_id):
        item = Item.objects.get(id=item_id)
        form = ItemUpdateForm(instance=item, files=request.FILES)
        return render(request, 'liberty_market/update_item.html', {'form': form})
