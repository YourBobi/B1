import os

from django.conf import settings
from django.utils.encoding import escape_uri_path
from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect, HttpResponse
from django.http.request import HttpRequest

from .models import Files, FileContents, FileClasses
from .db_repositoy.set_excel import Excel
from .db_repositoy.get_excel import DBExcel


def home_page(request):
    """
    Открытие главной страницы

    :param request:
    :return: home.html
    """
    return render(request, 'excel_app/general_pages/home.html')


def files_list(request: HttpRequest):
    """
    Открытие страницы со списком файлов. Так же сохранение данных в бд после нажатия кнопки.

    :param request:
    :return: excel_files.html
    """
    if request.method == "POST":
        try:
            file = request.FILES.get('xls')
            exel_to_db = Excel(str(file), 'Sheet1', file)
            exel_to_db.set_info()
        except Exception as e:
            print(e)

    return render(request, 'excel_app/general_pages/excel_files.html', context={'files': Files.objects.all()})


def table_page(request, file_id):
    """
    Страница с данными файла в виде таблицы. Скачать данную таблицу как excel.

    :param request:
    :param file_id: id файла в бд.
    :return:excel_table.html
    """
    file_contents = FileContents.objects.filter(file_id=file_id)
    data = DBExcel(file_id)
    data.get_data()  # чтение бд в data.data как pandas.DataFrame()
    file_path = os.path.join(settings.MEDIA_ROOT,  "temp\\" + Files.objects.get(id=file_id).name)

    if os.path.exists(file_path):
        os.remove(file_path)
        print("exist")

    if request.method == "POST":
        data.to_excel(file_path)
        with open(file_path, 'rb') as fh:
            name = str(Files.objects.get(id=file_id).name)
            print(name)
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'attachment; filename=''' + escape_uri_path(name)
            return response

    return render(request, 'excel_app/general_pages/excel_table.html',
                  context={'content': file_contents,
                           'data_html': data.to_html(),
                           'data_frame': data.get_data()})

