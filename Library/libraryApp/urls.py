"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('booklist/', views.book_list, name='bookList'),
    path('bookdetails/<int:book_id>/', views.book_details, name='bookDetail'),
    path('authorlist/', views.AuthorListView.as_view(), name='authorList'),
    path('createbook/',views.createBook,name='createBook'),
    path('createauthor/',views.createAuthor.as_view(),name='createAuthor'),
    path('updatebook/<int:book_id>',views.updateBook,name='updateBook')
    ]

