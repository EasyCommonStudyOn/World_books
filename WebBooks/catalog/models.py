"""
1.При проектировании моделей данных имеет смысл создавать самостоятельные модели
для каждого объекта. Под объектом мы будем понимать группу связанной информации.
В нашем случае очевидными объектами являются: жанры книг, сами книги, авторы,
издательства, экземпляры книг, язык.

2.определить, какие данные можно и желательно выдавать в виде списка
выбора

3.Как только будет определен перечень моделей данных (таблицы БД и поля таблиц),
нужно подумать об отношениях между моделями (между таблицами в БД). Django позволяет определять отношения «один к одному
» (конструктор OneToOneFielct), «один ко многим» (конструктор ForeignKey) и «многие
ко многим» (конструктор мanyТoManyField).

4.Минимально в каждой модели должен быть определен
стандартный метод класса для Python: _ str _ (). Это необходимо для того, чтобы
вернуть удобно читаемую строку для каждого объекта.
def str (self):
    return self.field name
Если необходимо вернуть несколько полей, то потребуется другая инструкция:
def str (self):
    return '%s, %s' % (self.field_name_l, self.field_name_2)

5.Еще один распространенный метод, который включается в модели Django, - метод
get_absolute_url (), который возвращает URL-aдpec для отображения отдельных записей
модели на веб-сайте. Если этот метод определен, то Django автоматически добавит
кнопку Просмотр на сайте на экранах редактирования записей модели (на сайте администратора).
Вот типичный шаблон для get_aЬsolute_url ():
def get_absolute_url(self):
    return reverse ( 'model-detail-view', args= [str (self. id)])

6.# Создать новую запись с помощью конструктора модели
a_record = MyModelName(my_field_name="КНИгa о вкусной еде")
# Сохраните запись в базе данных.
a_record.save()

7.Для поиска и выборки данных из БД в Django служит
объект Queryset. Это интегрирующий объект - он содержит несколько объектов,
которые можно перебирать (прокручивать). Чтобы извлечь все записи из таблицы базы
данных, вызовите метод objects.all().

8.Метод filter () позволяет отфильтровать данные для Queryset в соответствии с указанным
полем и критерием фильтрации

9.

10.


"""
from django.db import models
from django.urls import reverse  # обеспечит получение абсолютных URL-aдpecoв
from django.contrib.auth.models import User
from datetime import date

"""
формирования справочника жанров книг.
"""


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text=" Введите жанр книги",
                            verbose_name="Жанр книги")  # оно будет выводиться на экран в формах рядом с полем name.

    def __str__(self):
        return self.name  # возвращающий имя жанра, которое будет внесено в конкретную запись.


"""
справочник языков книг
"""


class Language(models.Model):
    name = models.CharField(max_length=20, help_text="Введите язык книги", verbose_name="Язык книги")

    def __str__(self):
        return self.name


"""
справочник издательств
"""


class Publisher(models.Model):
    name = models.CharField(max_length=20, help_text=" Введите наименование издательства", verbose_name="Издательство")

    def __str__(self):
        return self.name


"""
справочник, в котором будем хранить сведения об авторах книг
"""


class Author(models.Model):
    first_name = models.CharField(max_length=100, help_text="Введите имя автора", verbose_name="Имя автора")
    last_name = models.CharField(max_length=100, help_text="Введите фамилию автора", verbose_name="Фамилия автора")
    date_of_birth = models.DateField(help_text="Введите дату рождения", verbose_name="Дата рождения", null=True,
                                     blank=True)  # Это поле может содержать пустое значение (null=True), т. е. не обязательно для заполния.
    about = models.TextField(help_text="Введите сведения об авторе", verbose_name="Сведения об авторе")
    photo = models.ImageField(upload_to='images', help_text="Загрузите фото автора", verbose_name="Фото автора",
                              null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


"""
Создание модели книги
"""


class Book(
    models.Model):  # модель «Книги» связана связью «один ко многим» со следующими моделями:□ «Жанр книги»;□ «Язык книги»;□ «Издательство».
    title = models.CharField(max_length=200, help_text="Введите название книги", verbose_name="Название книги")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, help_text="Выберите жанр для книги",
                              verbose_name="Жанр книги", null=True)  # по первичному ключу связано с моделью Genre.
    language = models.ForeignKey(Language, on_delete=models.CASCADE, help_text="Выберите язык книги",
                                 verbose_name="Язык книги", null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, help_text="Выберите издательство",
                                  verbose_name="Издательство", null=True)
    year = models.CharField(max_length=4, help_text="Введите год издания", verbose_name="Год издания")
    authors = models.ManyToManyField(Author, help_text="Выберите автора (авторов) книги",
                                     verbose_name="Автор (авторы) книги")
    summary = models.TextField(max_length=1000, help_text="Введите краткое описание книги",
                               verbose_name="Аннотация книги")
    isbn = models.CharField(max_length=13, help_text="Должно содержать 13 символов", verbose_name="ISBN книги")
    price = models.DecimalField(decimal_places=2, max_digits=7, help_text="Введите цену книги (в рублях)",
                                verbose_name="Цена (руб.)")
    photo = models.ImageField(upload_to='images', help_text="Загрузите изображение обложки",
                              verbose_name="Изображение обложки", null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):  ## Возвращает URL-aдpec для доступа к определенному экземпляру книги
        return reverse('book-detail', args=[str(self.id)])

    def display_author(
            self):  # Для того чтобы сформировать список авторов книги, мы добавим функцию (метод) display_author в модели данных вооk. Эта функция станетформировать строку, в которой будут представлены все авторы книги.
        return ', '.join([author.last_name for author in
                          self.authors.all()])  # В этой функции организован цикл с инструкцией for. В теле цикла выбираются все авторы, связанные с данной книгой, из них формируется список, который будет возвращен в точку вызова.

    display_author.short_description = 'Авторы'


"""
Создание модели Status - состояние экземпляра книги
"""


class Status(models.Model):
    name = models.CharField(max_length=20, help_text="Введите статус экземпляра книги",
                            verbose_name="Статус экземпляра книги")

    def __str__(self):
        return self.name


"""
соэдание модели Booklnstance (экземпляр книги)
"""


class BookInstance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.SET_NULL,
                             null=True)  # Для названия книги создано поле ьооk, значение для него будет подгружено из модели вооk, с которой имеется связь по первичному ключу.
    inv_nom = models.CharField(max_length=20, null=True, help_text="Введите инвентарный номер экземпляра",
                               verbose_name="Инвентарный номер")
    status = models.ForeignKey('Status', on_delete=models.CASCADE, null=True,
                               help_text='Изменить состояние экземпляра',
                               verbose_name="Статус экземпляра книги")  # Для задания статуса экземпляра книги (на складе, в заказе, продана и пр.) предусмотрено поле status, значение для него будет подгружено из модели Status, с которой имеется связь по первичному ключу.
    due_back = models.DateField(null=True, blank=True, help_text="Введите конец срока статуса",
                                verbose_name="Дата окончания статуса")  # Для задания даты окончания действия статуса для экземпляра книги
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 verbose_name="Заказчик",
                                 help_text="Выберите заказчика книги")
    objects = models.Manager

    class Meta:
        ordering = [
            "due_back"]  # Для сортировки экземпляров книг создан класс меtа, при этом все экземпляры будут отсортированы по дате окоцчания действия статуса.

    def __str__(self):
        return '%s %s %s' % (self.inv_nom, self.book,
                             self.status)  # представляет объект Bookinstance, который будет выводить содержимое нескольких полей: название книги, ее инвентарный номер и статус.

    @property
    def is_overdue(self):    #Здесь проверяется условие - не превысило ли значение даты возврата книги текущей даты. В зависимости от значений этих дат будут возвращаться значения тrue или False.
        if self.due_back and date.today() > self.due_back:
            return True
        return False


