from django.urls import path
from .views import index, BookListView, BookDetailView, AuthorListView, AuthorDetailView, about, contact, \
    LoanedBooksByUserListView, edit_authors, add_author

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
    path('authors_add/', add_author, name='authors_add'),

]
