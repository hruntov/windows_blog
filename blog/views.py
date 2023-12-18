from django.http import HttpResponse
from django.shortcuts import render
from faker import Faker


fake = Faker()

menu = [{'title': 'Home', 'url_name': 'home'},
        {'title': 'About', 'url_name': 'about'},
        {'title': 'Blog', 'url_name': 'blog'},
        {'title': 'Contact', 'url_name': 'contact'},
        {'title': 'Login', 'url_name': 'login'},
        {'title': 'Add post', 'url_name': 'add_post'}
        ]


data_db = [
    {'id': 1, 'title': 'First article', 'text': fake.paragraph(nb_sentences=50)},
    {'id': 2, 'title': 'Second article', 'text': fake.paragraph(nb_sentences=50)},
    {'id': 3, 'title': 'Third article', 'text': fake.paragraph(nb_sentences=50)},
]


def blog(request):
    data = {
        'title': 'Blog',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'blog/blog.html', context=data)


def categories(request, category_id):
    return HttpResponse(f"{category_id}")


def categories_by_slug(request, category_slug):
    if request.GET:
        print(request.GET)

    return HttpResponse(f'<h1>{category_slug}</h1>')


def post(request, id):
    return HttpResponse(f"{id}")


def page_not_found(request, exception):
    return HttpResponse('<h1>Page not found</h1>', status=404)


def home(request):
    data = {
        'title': 'Blog',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'blog/home.html', context=data)


def about(request):
    return HttpResponse("About")


def contact(request):
    return HttpResponse("Contact")


def login(request):
    return HttpResponse("Login")


def add_post(request):
    return HttpResponse("Add post")
