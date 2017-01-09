from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Book, Category


def book_list_view(request, category=None):

    book_list_queryset = Book.objects.all()

    if category:
        book_list_queryset = book_list_queryset.filter(
            category__name=category)

    paginator = Paginator(book_list_queryset, 4)

    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:  #
        page_obj = paginator.page(paginator.num_pages)

    return render(request, "books/book_list.html",
                  {
                      'book_list': page_obj,
                      'categories': Category.objects.all(),
                      'page_obj': page_obj
                  })


