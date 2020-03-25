import requests
from requests.compat import quote_plus
from django.shortcuts import render
from bs4 import BeautifulSoup

BASE_CRAIGLIST_URL = 'https://manila.craigslist.org/search/{filter}?query={search_text}'
CRAIGLIST_IMG_URL = 'https://images.craigslist.org/{}_300x300.jpg'


def home(request):
    return render(request, 'iprocarlo_app/home.html')


def new_search(request):
    search_text = request.POST.get('search')
    filter = request.POST.get('value')
    filter_name_len = len(filter) + 1
    filter_name = request.POST.get('value')[5:filter_name_len]
    filter_code = request.POST.get('value')[0:3]

    final_url = BASE_CRAIGLIST_URL.format(filter=quote_plus(filter_code), search_text=quote_plus(search_text))

    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')

    post_listings = soup.find_all('li', {'class': 'result-row'})

    final_postings = []

    for post in post_listings:
        post_title = post.find(class_='result-title').text
        post_date = post.find(class_='result-date').text
        post_link = post.find('a').get('href')

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
