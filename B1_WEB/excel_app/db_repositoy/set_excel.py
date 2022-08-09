import pandas as pd
from ..models import FileClasses, FileContents, Files, IncomingBalance, OutgoingBalance, TurnOver, \
    ContentCharacteristics
from django.utils import timezone
from django.utils.timezone import make_aware
from datetime import datetime


class Excel:
    """
    Класс для записи информации из Excel файла в бд
    """
    def __init__(self, name: str, sheet_name: str, file):
        """
        Конструктор

        :param name: Имя файла
        :param sheet_name: Название страницы в Excel
        :param file: файл с информацией
        """
        self.body = pd.read_excel(file, sheet_name=sheet_name, skiprows=7)
        self.head = pd.read_excel(file, sheet_name=sheet_name).head()
        self.file_name = name
        self.sheet_name = sheet_name

    def set_info(self):
        """
        Set info in db

        :return: None
        """
        start_period = make_aware(datetime.strptime(self.head.values[1][0].split()[3], '%d.%m.%Y'))
        end_period = make_aware(datetime.strptime(self.head.values[1][0].split()[5], '%d.%m.%Y'))
        date = make_aware(datetime.strptime(str(self.head.values[4][0]), '%Y-%m-%d %H:%S:%M'))
        content = ContentCharacteristics.objects.create(bank=self.head.keys()[0],
                                                        start_period=start_period,
                                                        end_period=end_period,
                                                        date=date,
                                                        currency=self.head.values[4][-1])
        files = Files.objects.create(name=self.file_name,
                                     date=timezone.now(),
                                     content_characteristics_id=content)

        n = 0

        for el in self.body.values:
            if isinstance(el[0], str) and 'КЛАСС ' in el[0]:
                n += 1
                file_classes = FileClasses.objects.create(num=n, name=el[0])

            elif isinstance(el[0], str) and el[0][0] == str(n) and len(el[0]) > 2:
                # incoming_balance
                incoming_balance = IncomingBalance.objects.create(activ=el[1], passive=el[2])
                outgoing_balance = OutgoingBalance.objects.create(activ=el[5], passive=el[6])
                turn_over = TurnOver.objects.create(debit=el[3], credit=el[4])

                FileContents.objects.create(bank_account=el[0],
                                            file_id=files,
                                            class_id=file_classes,
                                            incoming_balance_id=incoming_balance,
                                            outgoing_balance_id=outgoing_balance,
                                            turn_over_id=turn_over)

    def get_body(self):
        """
        Get body

        :return: self.boby
        """
        return self.body

    def get_data(self):
        """
        Get data

        :return: self.body
        """
        return self.body

    def get_head(self):
        """
        Get head

        :return: self.head
        """
        return self.head
