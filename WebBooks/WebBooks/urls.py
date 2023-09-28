"""
1.Первое,
что нам необходимо сделать, - это определить, какую информацию мы бы хотели
показывать на наших страницах. Затем установить URL-aдpeca для получения соответствующих
ресурсов. После чего создать URL-преобразования, представления (функции
или классы) и шаблоны соответствующих страниц.

2.Сформируем
URL-aдpeca, которые понадобятся для наших страниц:
□ index/ - домашняя (индексная) страница;
□ index/Ьooks/ - список всех книг;
□ index/authors/ - список всех авторов;
□ index/Ьook/<id> - детальная информация для определенной книги со значением
первичного ключа, равным <id>. Например: /index/Ьook/3 для id = 3;
□ index/author/<id> - детальная информация для определенного автора со значением
первичного ключа, равным <id>. Например: /index/author/11 для автора с id = 11.

3.

4.

"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),  # def index(request): return HttpResponse("Глaвнaя страница сайта 'Мир книг'")

]

"""
Здесь выполнен импорт модуля settings и переменных, определяющих пути к медиафайлам,
и эти пути добавлены в диспетчер URL-aдpecoв. Здесь используется инструкция
if settings. DEBUG, т. е. подключение этих адресов будет происходить только тогда,
когда выполняется разработка и отладка программного кода.
"""
if settings.DEBUG:
    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
