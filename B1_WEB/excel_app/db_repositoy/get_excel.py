from ..models import FileContents, FileClasses, Files
import pandas as pd
import warnings


class DBExcel:
    """
    Класс для чтения информации из бд в excel формат или в html table
    """

    def __init__(self, file_id):
        """
        Конструктор

        :param file_id: id файла в бд
        """
        self.file = Files.objects.get(id=file_id)
        self.file_contents = FileContents.objects.filter(file_id=file_id)
        self.file_classes = FileClasses.objects.all()
        self.data = pd.DataFrame(columns=['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.list_of_num = []
        for el in self.file_contents:
            self.list_of_num.append(el.bank_account)
        self.set_table_content()

    def to_excel(self, link):
        """
        Made excel file

        :param link: Ссылка на сохоранение
        :return: file
        """
        return self.data.to_excel(link, na_rep='', index=False, header=False)

    def to_html(self):
        """
        Made html file

        :return: html file with table
        """
        return self.data.to_html(classes='col-md-12 table-bordered table-striped table-condensed cf',
                                 na_rep='', index=False, header=False)

    def get_data(self):
        """
        Get data

        :return: self.data
        """
        return self.data

    def set_table_content(self):
        """
        Запись данных из бд для определенного file_id в self.data в виде pandas.DataFrame

        :return: None
        """
        warnings.filterwarnings("ignore")
        number_of_class = '1'
        number_of_group_acc = '10'
        group_sum = {'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0}
        class_sum = {'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0}
        all_sum = {'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0}
        self.data = self.data.append({'A': self.file.content_characteristics_id.bank},
                                     ignore_index=True)
        self.data = self.data.append({'A': "Оборотная ведомость по балансовым счетам"}, ignore_index=True)
        self.data = self.data.append({'A': "за период с " +
                                           self.file.content_characteristics_id.start_period.strftime("%d.%m.%Y") +
                                           " по " +
                                           self.file.content_characteristics_id.end_period.strftime("%d.%m.%Y")},
                                     ignore_index=True)
        self.data = self.data.append({'A': "по банку"}, ignore_index=True)
        self.data = self.data.append({'A': ""}, ignore_index=True)
        self.data = self.data.append({'A':self.file.content_characteristics_id.end_period.strftime("%Y-%m-%d %H:%S:%M"),
                                      'G': self.file.content_characteristics_id.currency}, ignore_index=True)
        self.data = self.data.append({'A': "Б/сч",
                                      'B': "ВХОДЯЩЕЕ САЛЬДО",
                                      'D': "ОБОРОТЫ",
                                      'F': 'ИСХОДЯЩЕЕ САЛЬДО'}, ignore_index=True)
        self.data = self.data.append({'B': "Актив",
                                      'C': "Пассив",
                                      'D': "Дебет",
                                      'E': "Кредит",
                                      'F': "Актив",
                                      'G': "Пассив"}, ignore_index=True)
        self.data = self.data.append({'A': self.file_contents.get(bank_account=self.list_of_num[0]).class_id.name},
                                     ignore_index=True)

        for num in self.list_of_num:
            try:
                obj = self.file_contents.get(bank_account=num)

                if num[0:2] != number_of_group_acc:
                    self.data = self.data.append({'A': number_of_group_acc,
                                                  'B': group_sum.get('B'),
                                                  'C': group_sum.get('C'),
                                                  'D': group_sum.get('D'),
                                                  'E': group_sum.get('E'),
                                                  'F': group_sum.get('F'),
                                                  'G': group_sum.get('G')}, ignore_index=True)
                    number_of_group_acc = num[0:2]
                    group_sum = {'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0}

                if num[0:1] != number_of_class:
                    self.data = self.data.append({'A': 'ПО КЛАССУ',
                                                  'B': class_sum.get('B'),
                                                  'C': class_sum.get('C'),
                                                  'D': class_sum.get('D'),
                                                  'E': class_sum.get('E'),
                                                  'F': class_sum.get('F'),
                                                  'G': class_sum.get('G')}, ignore_index=True)

                    number_of_class = num[0:1]
                    number_of_group_acc = num[0:2]

                    class_sum = {'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0}

                    self.data = self.data.append({'A': obj.class_id.name},
                                                 ignore_index=True) if num != self.list_of_num[-1] else self.data

                self.data = self.data.append({'A': obj.bank_account,
                                              'B': obj.incoming_balance_id.activ,
                                              'C': obj.incoming_balance_id.passive,
                                              'D': obj.turn_over_id.debit,
                                              'E': obj.turn_over_id.credit,
                                              'F': obj.outgoing_balance_id.activ,
                                              'G': obj.outgoing_balance_id.passive}, ignore_index=True)

                group_sum['B'] += obj.incoming_balance_id.activ
                group_sum['C'] += obj.incoming_balance_id.passive
                group_sum['D'] += obj.turn_over_id.debit
                group_sum['E'] += obj.turn_over_id.credit
                group_sum['F'] += obj.outgoing_balance_id.activ
                group_sum['G'] += obj.outgoing_balance_id.passive
                class_sum['B'] += obj.incoming_balance_id.activ
                class_sum['C'] += obj.incoming_balance_id.passive
                class_sum['D'] += obj.turn_over_id.debit
                class_sum['E'] += obj.turn_over_id.credit
                class_sum['F'] += obj.outgoing_balance_id.activ
                class_sum['G'] += obj.outgoing_balance_id.passive
                all_sum['B'] += obj.incoming_balance_id.activ
                all_sum['C'] += obj.incoming_balance_id.passive
                all_sum['D'] += obj.turn_over_id.debit
                all_sum['E'] += obj.turn_over_id.credit
                all_sum['F'] += obj.outgoing_balance_id.activ
                all_sum['G'] += obj.outgoing_balance_id.passive


            except:
                continue

        self.data = self.data.append({'A': number_of_group_acc,
                                      'B': group_sum.get('B'),
                                      'C': group_sum.get('C'),
                                      'D': group_sum.get('D'),
                                      'E': group_sum.get('E'),
                                      'F': group_sum.get('F'),
                                      'G': group_sum.get('G')}, ignore_index=True)
        self.data = self.data.append({'A': 'ПО КЛАССУ',
                                      'B': class_sum.get('B'),
                                      'C': class_sum.get('C'),
                                      'D': class_sum.get('D'),
                                      'E': class_sum.get('E'),
                                      'F': class_sum.get('F'),
                                      'G': class_sum.get('G')}, ignore_index=True)
        self.data = self.data.append({'A': 'БАЛАНС',
                                      'B': all_sum.get('B'),
                                      'C': all_sum.get('C'),
                                      'D': all_sum.get('D'),
                                      'E': all_sum.get('E'),
                                      'F': all_sum.get('F'),
                                      'G': all_sum.get('G')}, ignore_index=True)

        pd.options.display.float_format = '{:,.2f}'.format
