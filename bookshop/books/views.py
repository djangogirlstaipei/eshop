from django.shortcuts import render
from .models import Book


def home(request):
    book_list = Book.objects.all()
    return render(request, 'home.html', {
        'book_list': book_list,
    })