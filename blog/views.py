from django.http import HttpResponse
from django.shortcuts import render
from faker import Faker


fake = Faker()

menu = {
        'home': 'Home',
        'about': 'About',
        'contact': 'Contact',
        'add_article': 'Add article',
        }

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


def post(request, post_slug):
    return HttpResponse(f"{post_slug}")


def page_not_found(request, exception):
    return HttpResponse('<h1>Page not found</h1>', status=404)
