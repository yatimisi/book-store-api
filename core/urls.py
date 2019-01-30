"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from books import views as book_views

from rest_framework import routers


router = routers.DefaultRouter()
router.trailing_slash = ''
router.register('books', book_views.BookViewSet)

urlpatterns = [
    # path('books/', book_views.index, name='book-index'),
    # path('books/<int:pk>/', book_views.show, name='book-show'),
    # path('books/add/', book_views.new , name='books-new'),
    # path('books/<int:pk>/edit/', book_views.edit, name='book-edit'),
    # path('books/<int:pk>/delete/', book_views.delete, name='book-delete'),

    # path('books', book_views.index, name='book-list'),
    # path('books/<int:pk>', book_views.detail, name='book-detail'),

    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
