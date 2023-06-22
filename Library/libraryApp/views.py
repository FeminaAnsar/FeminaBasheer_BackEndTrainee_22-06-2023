
from django.shortcuts import render
from .models import Book,Author
from django.http import HttpResponse
from .forms import CreateBook,CreateAuthor
from django.views.generic import ListView,CreateView,UpdateView
from django.urls import reverse
from django.shortcuts import redirect
from django.template import loader
import requests


def home(request):
    return render(request,'libraryApp/home.html')

def book_list(request):
        books= Book.objects.all()
        context={
            "books":books
        }
        return render(request,'libraryApp/booklist.html',context)

def book_details(request,book_id):
    try:
        books = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return HttpResponse("Book not found")
    return render(request,'libraryApp/bookdetails.html',{"book":books})

class AuthorListView(ListView):
    template_name="libraryApp/author.html"
    queryset=Book.objects.all()
    context_object_name="all_books"

def createBook(request):
        form=CreateBook()
        if request.method=="POST":
            form=CreateBook(request.POST)
            if form.is_valid():
                form.save()
                return redirect(createBook)
        context={"form":form}
        return render(request,"libraryApp/createbook.html",context)

class createAuthor(CreateView):
    template_name = "libraryApp/createauthor.html"
    form=CreateAuthor()
    queryset=Author.objects.all()
    fields='__all__'
    def get_success_url(self) -> str:
        return reverse('createAuthor')

def updateBook(request,book_id):
  book = Book.objects.get(id=book_id)
  template = loader.get_template('libraryApp/updatebook.html')
  context = {
    'book': book
  }
  return render(request, "libraryApp/updatebook.html", context)

# Create your views here.
