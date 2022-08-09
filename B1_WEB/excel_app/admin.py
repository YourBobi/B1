from django.contrib import admin
from .models import Files, FileClasses, FileContents,\
    IncomingBalance, OutgoingBalance, TurnOver

admin.site.register(Files)
admin.site.register(FileClasses)
admin.site.register(FileContents)
admin.site.register(IncomingBalance)
admin.site.register(OutgoingBalance)
admin.site.register(TurnOver)
