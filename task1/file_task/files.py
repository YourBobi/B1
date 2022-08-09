from task1.file_task.contents import ContentGenerator
import os
import threading


class FileGenerator:
    """
    Класс генерации файлов
    """
    def __init__(self, number_of_rows: int = 1, number_of_files: int = 1):
        self.number_of_files = number_of_files
        self.row_generator = ContentGenerator(number_of_rows)

    def write(self, link: str):
        """Сохранение файлов

        :param link: ссылка для сохранения
        :return: None
        """
        for i in range(self.number_of_files):
            with open(f'{link}/{i}.txt', 'w') as file:
                file.write(self.row_generator.get_content())


class FileManager:

    def __init__(self, link_from : str, link_to : str, file_name: str = "file_task.txt"):
        """
        :param link_from: Ссылка откуда берутся файлы
        :param link_to: Ссылка для сохранения файла со всей информацией
        :param file_name: Название файла
        """
        self.link_from = link_from
        self.link_to = link_to
        self.name = file_name
        self.content = ""
        self.set_content_from_files()

    def write(self):
        with open(f'{self.link_to}/{self.name}', 'w') as file:
            file.write(self.content)

    def delete_rows(self, search_string: str):
        """
        Удаление строк, в которых содержится search_string

        :param search_string: искомая строка
        :return: список строк, где была search_string
        """
        indexes = []
        for i in range(len(self.content)):
            if search_string in self.content[i]:
                indexes.append(i)

        self.content = [self.content[i] for i in range(len(self.content)) if i not in indexes]

        return indexes

    def set_content_from_files(self):
        """
        Запись файла

        :return: None
        """
        files = os.listdir(self.link_from)
        for file in files:
            self.__read_file__(f'{self.link_from}/{file}')

    def __read_file__(self, link):
        with open(link, 'r') as fb:
            self.content +=f"{fb.read()}\n"

    def get_content(self):
        return self.content.strip()
