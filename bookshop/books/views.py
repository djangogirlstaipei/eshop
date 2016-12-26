from django.views.generic import ListView
from books.models import Book, Category


class BooksListView(ListView):

    model = Book

    def get_context_data(self, **kwargs):
        context = super(BooksListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

books_view = BooksListView.as_view()
