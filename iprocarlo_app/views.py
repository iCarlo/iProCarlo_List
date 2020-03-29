import requests
from requests.compat import quote_plus
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from django.utils import timezone
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import CreateUserForm


BASE_CRAIGLIST_URL = 'https://manila.craigslist.org/search/{filter}?query={search_text}'
CRAIGLIST_IMG_URL = 'https://images.craigslist.org/{}_300x300.jpg'


@unauthenticated_user
def register(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_name = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user_name)

            set_group = Group.objects.get(name='customers')

            user.groups.add(set_group)

            return redirect('/login')

    register_form = {
        'form': form,
    }

    return render(request, 'iprocarlo_app/register.html', register_form)


@unauthenticated_user
def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password is incorrect!')

    return render(request, 'iprocarlo_app/login.html')


def logout_page(request):
    logout(request)
    return redirect('/login')


def user_page(request):
    return render(request, 'iprocarlo_app/user.html')


@login_required(login_url='/login')
@allowed_users(allowed_roles=['admins', 'customers'])
def home(request):
    return render(request, 'iprocarlo_app/home.html')


@login_required(login_url='/login')
@allowed_users(allowed_roles=['admins', 'customers'])
def new_search(request):
    search_text = request.POST.get('search')
    date = timezone.now()

    search_object = models.Search.objects.create(search_item=search_text, search_date=date)
    search_object.save()

    filter = request.POST.get('value')
    filter_name_len = len(filter) + 1
    filter_name = request.POST.get('value')[5:filter_name_len]
    filter_code = request.POST.get('value')[0:3]

    models.Filter.objects.create(filter_text=filter_name, searched=search_object)

    final_url = BASE_CRAIGLIST_URL.format(filter=quote_plus(filter_code), search_text=quote_plus(search_text))

    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')

    post_listings = soup.find_all('li', {'class': 'result-row'})

    final_postings = []

    for post in post_listings:
        post_title = post.find(class_='result-title').text
        post_link = post.find('a').get('href')

        if post.find(class_='result-date'):
            post_date = post.find(class_='result-date').text
        else:
            post_date = "Date N/A"

        if post.find(class_='result-hood'):
            post_place = post.find(class_='result-hood').text
        else:
            post_place = "(Place N/A)"

        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = "Price N/A"

        if post.find(class_='result-image').get('data-ids'):
            post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            post_image_url = CRAIGLIST_IMG_URL.format(post_image_id)
        else:
            post_image_url = 'https://www.craigslist.org/images/peace.jpg'

        final_postings.append((post_title, post_date, post_link, post_place, post_price, post_image_url))

    data_scrape = {
        'search_text': search_text,
        'filter_name': filter_name,
        'final_postings': final_postings,
    }
    return render(request, 'iprocarlo_app/new_search.html', data_scrape)
