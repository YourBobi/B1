from datetime import datetime

from task1.file_task.files import FileManager
from task1.db.base import get_db, engine, Base
from task1.db.models.table1 import Table1Model
from sqlalchemy.orm import Session
from tqdm import tqdm

"""
Файл для общения с БД
"""


def import_in_db(db: Session = next(get_db()), content = ""):
    """
    Запись данных с файла в бд
    :param db: бд
    :param content: FileManager.get_content()
    :return: None
    """
    content = content.split()

    for i in tqdm(range(len(content)), desc="Добавление объектов в сессию…", ascii=False, ncols=120):

        list_row = content[i].split("||")
        db.add(Table1Model(datetime.strptime(list_row[0], "%Y.%m.%d"),
                           list_row[1],
                           list_row[2],
                           list_row[3],
                           list_row[4]))

    print("Сохранение")
    db.commit()


def create_table1(py_engine=engine):
    """
    Создание таблицы в бд из созданных ранее моделей в ../models/table1.py
    :param py_engine:
    :return: None
    """
    Base.metadata.create_all(py_engine)


def get_sum_int_numbers(db: Session = next(get_db())):
    """
    Сумма всех целых чисел в table1

    :param db: db
    :return: сумма всех целых чисел
    """
    return db.execute("SELECT SUM(int_numbers) FROM Table1").one()[0]


def get_avg_float_numbers(db: Session = next(get_db())):
    """
    Медиана всех дробных чисел

    :param db:
    :return:int
    """
    return db.execute("SELECT AVG(float_numbers) FROM Table1").one()[0]
