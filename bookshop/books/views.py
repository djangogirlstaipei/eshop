from django.views.generic import ListView
from .models import Book


# def home(request):
#     book_list = Book.objects.all()
#     return render(request, 'home.html', {
#         'book_list': book_list,
#     })


home = ListView.as_view(model=Book)
