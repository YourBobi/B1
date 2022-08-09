from task1.file_task.files import FileManager, FileGenerator
from task1.db.repository.table1 import *


def task1():
    """
    1.	Сгенерировать 100 текстовых файлов

    :return None
    """
    g = FileGenerator(number_of_files=100, number_of_rows=10000)
    g.write("./txt_files")


def task2():
    """
    2.	Реализовать объединение файлов в один с выводом удаленных строк.
    :return: None
    """
    content = FileManager(link_from="./txt_files", link_to="./", file_name="test.txt")
    print(content.delete_rows("2018"))
    content.write()


def task3():
    """
    3. Импорт в СУБД SQLITE
    :return:None
    """
    # создание таблицы и бд
    create_table1()

    # Запись
    content = FileManager(link_from="./txt_files", link_to="./", file_name="test.txt")
    import_in_db(content=content.get_content())


def task4():
    """
    4.	Сумма всех целых чисел и медиану всех дробных чисел.
    :return:None
    """
    print("Сумма всех целых чисел: ", get_sum_int_numbers())
    print("Медиана: ", get_avg_float_numbers())
