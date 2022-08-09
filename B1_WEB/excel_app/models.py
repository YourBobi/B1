from django.db import models


# Для работы с DBExcel файлами


class ContentCharacteristics(models.Model):
    bank = models.CharField(max_length=250)
    start_period = models.DateField()
    end_period = models.DateField()
    date = models.DateTimeField()
    currency = models.CharField(max_length=250)

    def __str__(self):
        return f"ContentCharacteristics <bank: \"{self.bank}\", start_period: \"{self.start_period}\", " \
               f"end_period:\"{self.end_period}\", date: \"{self.date}\", currency: \"{self.currency}\">"


class Files(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    content_characteristics_id = models.ForeignKey(ContentCharacteristics, on_delete=models.CASCADE)

    def __str__(self):
        return f"Files<name: \"{self.name}\", date: \"{self.date}\">"


class FileClasses(models.Model):
    num = models.IntegerField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"FileClasses<name: \"{self.name}\", number: \"{self.num}\">"


class IncomingBalance(models.Model):
    activ = models.FloatField()
    passive = models.FloatField()

    def __str__(self):
        return f"IncomingBalance<active: \"{self.activ}\", passive: \"{self.passive}\">"


class OutgoingBalance(models.Model):
    activ = models.FloatField()
    passive = models.FloatField()

    def __str__(self):
        return f"OutgoingBalance<active: \"{self.activ}\", passive: \"{self.passive}\">"


class TurnOver(models.Model):
    debit = models.FloatField()
    credit = models.FloatField()

    def __str__(self):
        return f"TurnOver<debit: \"{self.debit}\", credit: \"{self.credit}\">"


class FileContents(models.Model):
    bank_account = models.CharField(max_length=250)
    file_id = models.ForeignKey(Files, on_delete=models.CASCADE)
    class_id = models.ForeignKey(FileClasses, on_delete=models.CASCADE)
    incoming_balance_id = models.ForeignKey(IncomingBalance, on_delete=models.CASCADE)
    outgoing_balance_id = models.ForeignKey(OutgoingBalance, on_delete=models.CASCADE)
    turn_over_id = models.ForeignKey(TurnOver, on_delete=models.CASCADE)

    def __str__(self):
        return f"FileContents <file_id: \"{self.file_id}\", class_id: \"{self.class_id}\", " \
               f"incoming_balance_id:\"{self.incoming_balance_id}\"," \
               f" outgoing_balance_id: \"{self.outgoing_balance_id}\", turn_over_id: \"{self.turn_over_id}\">"
