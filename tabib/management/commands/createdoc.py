from django.core.management.base import BaseCommand
from tabib.models import User, Doctor, WorkTime
from faker import Faker
import datetime

date1start = datetime.datetime.now()
date1end = date1start + datetime.timedelta(hours=2)
date2start = date1start + datetime.timedelta(days=1)
date2end = date2start + datetime.timedelta(hours=1)


class Command(BaseCommand):
    help = 'creating 4000 fake doctor'

    def handle(self, *args, **options):
        fake = Faker()
        counter = 1
        while counter <= 5000:
            user_name = fake.first_name()
            user_lastname = fake.last_name()
            myuser = User.objects.create(name=user_name, last_name=user_lastname)
            myuser.save()
            mydoctor = Doctor.objects.create(name=user_name, last_name=user_lastname, user=myuser)
            mydoctor.save()
            myworktime = WorkTime.objects.create(doctor=mydoctor, apointment_time=30, week_avalible=1,
                                                 wensday_start=date1start, wensday_end=date1end,
                                                 tursday_start=date2start, tursday_end=date2end)
            myworktime.save()
            print('create %s doctor'%counter)
            counter += 1
        self.stdout.write(self.style.SUCCESS('Successfully add "%s" doctors' % counter))
