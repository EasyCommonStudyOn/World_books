"""
1.Представление (view)- это программный модуль, который обрабатьmает НТТРзапрос,
поступивший от пользователя. Представление может быть реализовано в виде
функции или класса, мы реализуем его в виде функции.

2.CBV (Class-Based Views). В Django имеется группа встроенных классов для представлений
(view), например:
□ Listview - просмотр списка объектов;
□ createview - создание конкретного объекта;
□ Formview - отображение формы;
□ DetailView - просмотр определенного объекта;
□ UpdateView - обновление конкретного объекта;
□ oeleteView - удаление конкретного объекта и т. п.

3.Djaпgo имеет отличный встроенный механизм для организации постраничного вьmода.
Более того, он встроен в класс ListView отображения списков

"""

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Author, BookInstance


def index(
        request):  # созданы две текстовые переменные text_heact и text_bocty, их значения загружены в объект context, который представляет собой словарь Python. Через функцию rencter этот словарь передан в ·шаблон НТМL-страницы catalog/index.html.

    """
    В первой части функции inctex () выполняются запросы к БД и выборка данных:
□ о книгах - books;
□ о количестве книг - num_books;
□ о числе экземпляров книг - num _ instances;
□ о числе экземпляров книг, доступных к продаже (находятся на складе)- num
instances_availaЫe;
□ об авторах книг - authors;
□ о числе авторов книг - num_authors.
Во второй части функции index () создается словарь context, в который загружаются все
данные, полученные из БД. Затем вызьmается функция render (), которая в качестве ответа
пользователю создает и возвращает НТМL-страницу index.html.
    """

    text_head = 'На этом сайте вы можете получить книги в электронном виде'
    books = Book.objects.all()  # Данные о книгах и их количестве
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()  # Данные об экземплярах книг в БД
    num_instances_available = BookInstance.objects.filter(
        status=2).count()  # Доступные книги (статус = 'На складе')
    authors = Author.objects  # Данные об авторах книг
    num_authors = Author.objects.count()
    # text_body = 'Это содержимое главной страницы сайта'
    context = {'text_head': text_head,
               'books': books,
               'num_books': num_books,
               'num_instances': num_instances,
               'num_instances_available': num_instances_available,
               'authors': authors, 'num_authors': num_authors}  # Словарь для передачи данных в шаблон index.html
    return render(request, 'catalog/index.html', context)


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    paginate_by = 3
    #пагинатор прописан в base html
    #Djaпgo имеет отличный встроенный механизм для организации постраничного вьmода.
# Более того, он встроен в класс ListView отображения списков, так что нам не придется
# продельmать большой объем работы, чтобы воспользоваться возможностями постраничного
# вьmода.

    """
     <div class="pagination">
                <span class="step-links">
                    {% if page_obj.paginator.num_pages > 1 %}
                    {% if page_obj.has_previous %}
                    <a href="?page=1">&laqua; Первая</a>  
                    <a href="?page={{ page_obj.previous_page_number }}">Предыдущая</a>
                    {% endif %}
                    <span class="current">
                        Стр. {{page_obj.number}}
                        из {{page_obj.paginator.num_pages}}.
                    </span>
                    {% of page_obj.has_next %}
                    <a href="?page={{ page_obj.next_page_number }}">Следующая</a>
                    <a href="?page={{ page_obj.paginator.num_pages }}">Предыдушая &raquo;</a>
                    {% endif %}
                    {% endif %}
                </span>
            </div>
    
    """

    """
    Здесь мы импортировали базовый класс (iпport ListView) и на его основе создали собственный
класс вookListView (ListView). Можно было бы обойтись всего одной строкой
кода - moctel = вооk (подключением модели данных Book). В созданном классе по умолчанию
будет сформирован ряд объектов, в частности:
□ object_list - список с данными о книгах, полученных из БД;
□ teпplate_name- имя шаблона для вьmода списка книг (по умолчанию book_list.html). 
Можно воспользоваться этими объектами, а при желании можно переопределить эти
имена, например:
context_object_name = 'books'
teпplate_name = "my_books.html"
В итоге созданный нами класс вookListView
выполнит запрос к базе данных, получит все записи о книгах из модели (вооk), а затем
передаст эти данные в шаблон book_list.html.
В этом шаблоне теперь из списка ьooks можно с использованием цикла получить данные
по любой книге: books. title - название книги, books. genre - жанр, books. year -
год издания и т. д.
    """


class BookDetailView(DetailView):
    model = Book
    context_object_nmae = 'book'
    """
    В созданном классе по
умолчанию будет сформирован ряд объектов, в частности:
□ obj ect - данные о конкретной книге, полученные из БД;
□ teщ:,late_name- имя шаблона для вывода информации о конкретной книге (по умол-
чанию book_detail.html).
Можно воспользоваться этими объектами, а при желании можно переопределить эти
имена, например:
context_object_name = 'book'
teщ:,late_name = "my_book.html"
В итоге созданный нами класс oetailview выполнит запрос к базе данных, получит данные
из БД о конкретной книге, а затем передаст эти данные в шаблон book_detail.html.
В этом шаблоне теперь из объекта Ьооk можно получить данные по конкретной книге:
book. title - название книги, book.genre - жанр, book.year- год издания и т. д.
    """


class AuthorListView(ListView):
    model = Author
    paginate_by = 4

