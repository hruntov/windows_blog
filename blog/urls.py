from django.urls import path

from blog import views
from blog.views import page_not_found

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('add_post/', views.add_post, name='add_post'),
    path('cats/<int:category_id>/', views.categories),
    path('cats/<slug:category_slug>/', views.categories_by_slug),
    path('post/<int:id>/', views.post, name='post'),
    ]
