import random
from datetime import datetime, timedelta
import string


class ContentGenerator:
    """
    Класс генерации случайных строк по примеру
    """
    def __init__(self, number_of_rows: int = 1):
        self.number_of_rows = number_of_rows

    def get_content(self):
        content = ""
        for i in range(self.number_of_rows):
            content += self.get_row() + "\n"
        return content.strip("\n")

    def get_row(self):
        row = f"{self.random_date().strftime('%Y.%m.%d')}||" \
              f"{self.random_latin_letters()}||" \
              f"{self.random_russian_letters()}||" \
              f"{self.random_integer_number()}||" \
              f"{self.random_float_number()}||"
        return row

    @staticmethod
    def random_date():
        """
        Случайная дата за последние 5 лет

        :return: date
        """
        end = datetime.now()
        start = end - timedelta(days=5*365)
        return start + (end - start) * random.random()

    @staticmethod
    def random_latin_letters():
        """Случайный набор 10 латинских символов

        :return: string
        """
        data = ""
        for _ in range(10):
            data += random.choice(string.ascii_letters)
        return data

    @staticmethod
    def random_russian_letters():
        """
        Случайный набор 10 русских символов

        :return: string
        """
        cyrillic_lower_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        cyrillic_letters = cyrillic_lower_letters + cyrillic_lower_letters.upper()
        data = ""

        for _ in range(10):
            data += random.choice(cyrillic_letters)
        return data

    @staticmethod
    def random_integer_number():
        """
        Случайное положительное четное целочисленное число в диапазоне от 1 до 100 000 000

        :return: int number
        """
        return random.randrange(1, 100000000)

    @staticmethod
    def random_float_number():
        """
        Случайное положительное число с 8 знаками после запятой в диапазоне от 1 до 20

        :return: float number
        """
        return round(random.uniform(1, 20), 8)
