from django.shortcuts import render

from .models import Book, Category


def book_list_view(request, category=None):

    book_list_queryset = Book.objects.all()

    if category:
        book_list_queryset = book_list_queryset.filter(
            category__name=category)


    return render(request, "books/book_list.html",
                  {
                      'book_list': book_list_queryset,
                      'categories': Category.objects.all(),
                  })
