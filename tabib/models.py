import datetime

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    def __str__(self):
        return "{} {}".format(self.name, self.last_name)



class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor')
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    def __str__(self):
        return "dr {}".format(self.last_name)


class WorkTime(models.Model):

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='worktime')
    apointment_time = models.IntegerField(default=30, blank=True, null=True)
    week_avalible = models.IntegerField(default=1, blank=True, null=True)

    saturday_start = models.DateTimeField(blank=True, null=True)
    saturday_end = models.DateTimeField(blank=True, null=True)

    sunday_start = models.DateTimeField(blank=True, null=True)
    sunday_end = models.DateTimeField(blank=True, null=True)

    monday_start = models.DateTimeField(blank=True, null=True)
    monday_end = models.DateTimeField(blank=True, null=True)

    tuesday_start = models.DateTimeField(blank=True, null=True)
    tuesday_end = models.DateTimeField(blank=True, null=True)

    wensday_start = models.DateTimeField(blank=True, null=True)
    wensday_end = models.DateTimeField(blank=True, null=True)

    tursday_start = models.DateTimeField(blank=True, null=True)
    tursday_end = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "work time {}".format(self.doctor.last_name)

    def save(self, *args, **kwargs):
        doc = self.doctor
        past = DayDetail.objects.filter(doctor=doc)
        past.delete()
        if self.apointment_time:
            ap_time = self.apointment_time
        else:
            ap_time = 30
        from datetime import timedelta
        for i in range(0, self.week_avalible):
            i = i*7
            if self.saturday_start:
                start = self.saturday_start + datetime.timedelta(days=i)
                while start < self.saturday_end + datetime.timedelta(days=i):
                    ap = DayDetail.objects.create(day='sa', datetime=start, doctor=doc)
                    ap.save()
                    start += timedelta(minutes=ap_time)

            if self.sunday_start :
                start = self.sunday_start + datetime.timedelta(days=i)
                while start < self.sunday_end + datetime.timedelta(days=i):
                    ap = DayDetail.objects.create(day='su', datetime=start, doctor=self.doctor)
                    ap.save()
                    start += timedelta(minutes=ap_time)

            if self.monday_start :
                start = self.monday_start + datetime.timedelta(days=i)
                while start < self.monday_end + datetime.timedelta(days=i):
                    ap = DayDetail.objects.create(day='mo', datetime=start, doctor=self.doctor)
                    ap.save()
                    start += timedelta(minutes=ap_time)

            if self.tuesday_start :
                start = self.tuesday_start + datetime.timedelta(days=i)
                while start < self.tuesday_end + datetime.timedelta(days=i):
                    ap = DayDetail.objects.create(day='tu', datetime=start, doctor=self.doctor)
                    ap.save()
                    start += timedelta(minutes=ap_time)

            if self.wensday_start:
                start = self.wensday_start + datetime.timedelta(days=i)
                while start < self.wensday_end + datetime.timedelta(days=i):
                    ap = DayDetail.objects.create(day='we', datetime=start, doctor=self.doctor)
                    ap.save()
                    start += timedelta(minutes=ap_time)

            if self.tursday_start:
                start = self.tursday_start + datetime.timedelta(days=i)
                while start < self.tursday_end + datetime.timedelta(days=i):
                    ap = DayDetail.objects.create(day='tur', datetime=start, doctor=self.doctor)
                    ap.save()
                    start += timedelta(minutes=ap_time)
        super().save(*args, **kwargs)




class ReservedApointment(models.Model):
    SATURDAY = 'sa'
    SUNDAY = 'su'
    MONDAY = 'mo'
    TUESDAY = 'tu'
    WENSDAY = 'we'
    TURSDAY = 'tur'
    TYPES = (
        (SATURDAY, 'شنبه'),
        (SUNDAY, '1شنبه'),
        (MONDAY, '2شنبه'),
        (TUESDAY, '3شنبه'),
        (WENSDAY, '4شنبه'),
        (TURSDAY, '5شنبه'),
    )
    day = models.CharField(max_length=3, choices=TYPES, default=SATURDAY)
    datetime = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor =  models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='apointments')
    def __str__(self):
        return "appointment {} {}".format(self.datetime, self.day)

    def save(self, *args, **kwargs):
        ap = DayDetail.objects.get(doctor=self.doctor, datetime=self.datetime)
        ap.delete()
        super().save(*args, **kwargs)



class DayDetail(models.Model):
    SATURDAY = 'sa'
    SUNDAY = 'su'
    MONDAY = 'mo'
    TUESDAY = 'tu'
    WENSDAY = 'we'
    TURSDAY = 'tur'
    TYPES = (
        (SATURDAY, 'شنبه'),
        (SUNDAY, '1شنبه'),
        (MONDAY, '2شنبه'),
        (TUESDAY, '3شنبه'),
        (WENSDAY, '4شنبه'),
        (TURSDAY, '5شنبه'),
    )
    day = models.CharField(max_length=3, choices=TYPES, default=SATURDAY)
    datetime = models.DateTimeField(null=True)

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='daydetail')
    def __str__(self):
        return "ap {} {}".format(self.datetime, self.day)


