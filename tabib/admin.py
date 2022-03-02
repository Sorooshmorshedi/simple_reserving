from django.contrib import admin
from tabib.models import Doctor, WorkTime, User, ReservedApointment, DayDetail

admin.site.register(Doctor)
admin.site.register(WorkTime)
admin.site.register(User)
admin.site.register(ReservedApointment)
admin.site.register(DayDetail)



