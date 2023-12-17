from django.http import HttpResponse
from django.shortcuts import render


def blog(request):
    context = {
        'name': 'Kostiantyn Hruntotv'
    }
    return render(request, 'blog/blog.html', context)


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
