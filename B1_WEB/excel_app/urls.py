from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('excel', views.files_list, name='exel_page'),
    path('excel/id=<int:file_id>', views.table_page, name='xls_table'),
]
