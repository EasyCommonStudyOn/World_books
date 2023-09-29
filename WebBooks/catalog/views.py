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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import AuthorForm


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
    num_visits = request.session.get('num_visits', 0)  # Число посещений этого view в sessions
    request.session[
        'num_visits'] = num_visits + 1  # В первую очередь мы формируем здесь переменную 'num visi ts' из сессии и устанавливаем
    # для нее значение о (если оно не бьшо установлено ранее). Затем каждый раз при
    # обращении к задействованному представлению (view) мы увеличиваем значение этой
    # переменной на единицу и сохраняем его в сессии (до следующего посещения этой
    # страницы пользователем).
    context = {'text_head': text_head,
               'books': books,
               'num_books': num_books,
               'num_instances': num_instances,
               'num_instances_available': num_instances_available,
               'authors': authors,
               'num_authors': num_authors,
               'num_visits': num_visits}  # Словарь для передачи данных в шаблон index.html
    return render(request, 'catalog/index.html', context)


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    paginate_by = 3
    # пагинатор прописан в base html
    # Djaпgo имеет отличный встроенный механизм для организации постраничного вьmода.
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


class AuthorDetailView(DetailView):
    model = Author


def about(request):
    text_head = 'Сведения о компании'
    name = 'Интеллектуальные информационные системы'
    rabl = 'Разработка приложений на основе ' \
           'систем искусственного интеллекта'
    rab2 = 'Распознавание объектов дорожной инфраструктуры'
    rab3 = 'Создание графических АРТ-объектов на основе ' \
           'систем искусственного интеллекта'
    rab4 = 'Создание цифровых интерактивных книг, учебных пособий ' \
           'автоматизированных обучающих систем'
    context = {
        'text_head': text_head,
        'name': name,
        'raЬl': rabl,
        'raЬ2': rab2,
        'raЬЗ': rab3,
        'raЬ4': rab4
    }
    return render(request, 'catalog/about.html', context)


def contact(request):
    text_head = 'Контакты'
    name = 'ООО "Интеллектуальные информационные системы"'
    address = 'Москва, ул. Планерная, д. 20, к. 1'
    tel = '495-345-45-45'
    email = 'iisinfo@mail.ru'

    # Dictionary to pass data to the 'contact.html' template
    context = {
        'text_head': text_head,
        'name': name,
        'address': address,
        'tel': tel,
        'email': email,
    }

    # Pass the 'context' dictionary to the 'contact.html' template
    return render(request, 'catalog/contact.html', context)


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(
            self):  # Чтобы получить только объекты вookinstance для текущего пользователя, мы реализуем здесь собственный метод get_queryset() (заказы пользователя).
        return BookInstance.objects.filter(borrower=self.request.user, status='2').order_by(
            'due_back')  # Обратите внимание, что параметр '2' в этом фильтре - это код справочника статусов В заказе.


def edit_authors(request):
    """
    Здесь создается объект author, в который из БД загружаются
сведения обо всех авторах. Этот объект упаковьmается в словарь context,
который затем передается в шаблон edit_authors.html.
    """
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, "catalog/edit_authors.html", context)


def add_author(request):
    """
    Здесь сначала импортируется форма Form_add_author и функция Django reverse, а затем
проверяется условие, какой запрос поступил от пользователя POST или GET.
Если поступил GЕТ-запрос (пользователь открьmает форму для ввода данных), то на
основе класса Form_add_author() создается объект form, который через контекстный словарь
context передается в шаблон catalog/authors_add.html.
Если поступил РОSТ-запрос (пользователь ввел данные и нажал кнопку Сохранить),
то сначала переменные ( first name, last _ name, date of Ьirth, about, photo) получают значе-
ния, которые пользователь ввел в поля формы, а затем на их основе создается специальный
объект ( obj), который записьmается в БД ( obj. save). После этого с помощью
функции reverse вызьmается страница со списком авторов (authors-list).
    """
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)  # Use the corrected form name
        if form.is_valid():
            # Extract data from the form
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            date_of_birth = form.cleaned_data.get("date_of_birth")
            about = form.cleaned_data.get("about")
            photo = form.cleaned_data.get("photo")

            # Create an object to write to the database
            obj = Author.objects.create(
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                about=about,
                photo=photo
            )
            obj.save()  # Save the data

            # Redirect to the authors list page
            return HttpResponseRedirect(reverse('authors-list'))
    else:
        form = AuthorForm()  # Use the corrected form name

    context = {"form": form}
    return render(request, "catalog/authors_add.html", context)
