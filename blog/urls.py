from django.urls import path

from blog import views
from blog.views import page_not_found

urlpatterns = [
    path('', views.blog, name='blog'),
    path('cats/<int:category_id>/', views.categories),
    path('cats/<slug:category_slug>/', views.categories_by_slug),
    path('post/<slug:post_slug>/', views.post),
    ]
