from rest_framework import serializers
from tabib.models import User, Doctor, WorkTime, DayDetail, ReservedApointment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class WorkTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTime
        fields = '__all__'

class DayDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayDetail
        fields = '__all__'

class ReservedApointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservedApointment
        fields = '__all__'


class DocWorkTime(serializers.ModelSerializer):
    class Meta:
        model = WorkTime
        fields = 'saturday_start', 'saturday_end', 'sunday_start', 'sunday_end',\
                 'monday_start', 'monday_end', 'tuesday_start', 'tuesday_end', 'wensday_start',\
                 'wensday_end', 'tursday_start', 'tursday_end'
        read_only_fields = ['saturday_start', 'saturday_end', 'sunday_start', 'sunday_end',
                            'monday_start', 'monday_end', 'tuesday_start', 'tuesday_end', 'wensday_start',
                            'wensday_end', 'tursday_start', 'tursday_end'
                            ]



class DocDayDetail(serializers.ModelSerializer):
    class Meta:
        model = DayDetail
        fields = 'id' , 'datetime'
        read_only_fields = ['datetime']

class DocapontmentDetail(serializers.ModelSerializer):
    class Meta:
        model = ReservedApointment
        fields = 'datetime', 'doctor', 'user'
        read_only_fields = ['datetime', 'doctor', 'user']



class AllDocSerializer(serializers.ModelSerializer):
    worktime = DocWorkTime(read_only=True, many=True)
    daydetail = DocDayDetail(read_only=True, many=True)
    apointments = DocapontmentDetail(read_only=True, many=True)
    class Meta:
        model = Doctor
        fields = 'id', 'user', 'name', 'last_name', 'worktime', 'daydetail', 'apointments'
        read_only_fields = ['id', 'user', 'name', 'last_name', 'worktime', 'daydetail', 'apointments']


class DoctorsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length = 150, read_only = True)
    last_name = serializers.CharField(max_length = 150, read_only = True)
    worktime = DocWorkTime(read_only=True, many=True)
    daydetail = DocDayDetail(read_only=True, many=True)
    apointments = DocapontmentDetail(read_only=True, many=True)




