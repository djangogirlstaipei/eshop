from django.views.generic import ListView, DetailView

from .models import Book, Category


class BooksListView(ListView):
    model = Book

    paginate_by = 10

    def categories(self):
        return Category.objects.all()

    def get_queryset(self):
        query_set = super(BooksListView, self).get_queryset()

        category = self.kwargs.get('category')

        if category:
            query_set = query_set.filter(category__name=category)

        return query_set


book_list_view = BooksListView.as_view()


class BookDetail(DetailView):
    model = Book


book_detail_view = BookDetail.as_view()
