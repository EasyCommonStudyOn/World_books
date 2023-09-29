from django.urls import path
from .views import index, BookListView, BookDetailView, AuthorListView, AuthorDetailView, about, contact, \
    LoanedBooksByUserListView, edit_authors, add_author, delete, edit_author, edit_books, BookCreate, BookUpdate, BookDelete

urlpatterns = [
    path('', index, name='index'),
    #     В функции path () определен параметр narne, который уникально объявляет, что мы имеем
    # дело с частным URL-преобразованием. После такого объявления можно использовать
    # это имя для «обратного» (reverse) преобразования, т. е. для динамического создания
    # URL-aдpeca, указывающего на определенный ресурс. Например, если мы задали
    # такое символическое имя, то теперь можно ссьmаться на нашу главную страницу сайта
    # при помощи создания следующей ссьmки внутри какого-либо НТМL-шаблона:
    # <а href="{% url 'index' %}">Главная страница</а>

    path('books/', BookListView.as_view(), name='books'),
    path('books/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    # Здесь угловые скобки< .. > необходимы для того, чтобы получить
    # значение из URL-aдpeca. Преобразователь int обеспечивает гарантированное получение
    # целочисленного параметра, а параметр pk (primary key- первичный ключ)
    # служит для получения идентификатора книги из БД.
    # Практически так же, как и для страницы сайта ьooks, функция path () связьmает маршрут (URL-aдpec) страницы (
    # ьooks/<int:pk>) с классом в представлении views.BookDetailView. as_ v iew () . Кроме того, здесь определено имя
    # для ссьmки на данную страницу сайта (name='book-detail').

    path('authors/', AuthorListView.as_view(), name='authors-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='authors-detail'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('mybooks/', LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('edit_authors/', edit_authors, name='edit_authors'),
    path('edit_author/<int:id>', edit_author, name='edit_author'),
    path('authors_add/', add_author, name='authors_add'),
    path('delete/<int:id>/', delete, name='delete'),
    path('edit_books/',edit_books, name='edit_books'),
    path('book/create/', BookCreate.as_view(), name="book_create"),
    path('book/update/<int:pk>', BookUpdate.as_view(), name="book_update"),
    path('book/delete/<int:pk>', BookDelete.as_view(), name="book_delete"),

]
