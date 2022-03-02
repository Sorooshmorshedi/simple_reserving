import datetime

from django.http import Http404
from rest_framework.views import APIView

from tabib.models import Doctor, WorkTime, ReservedApointment, DayDetail, User
from tabib.serializers import DoctorSerializer, WorkTimeSerializer, ReservedApointmentSerializer, \
    DayDetailSerializer, UserSerializer, DoctorsSerializer

from rest_framework import status
from rest_framework.response import Response


from django.template import loader
from django.http import HttpResponse

from rest_framework_extensions.cache.decorators import cache_response


class UserApiView(APIView):
    def get(self, request):
        query = User.objects.all()
        serializers = UserSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        query = self.get_object(pk)
        serializers = UserSerializer(query)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        query = self.get_object(pk)
        serializer = UserSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        query = self.get_object(pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DoctorApiView(APIView):
    def get(self, request):
        query = Doctor.objects.all()
        serializers = DoctorSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorDetail(APIView):
    def get_object(self, pk):
        try:
            return Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        query = self.get_object(pk)
        serializers = DoctorSerializer(query)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        query = self.get_object(pk)
        serializer = DoctorSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        query = self.get_object(pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WorkTimeApiView(APIView):
    def get(self, request):
        query = WorkTime.objects.all()
        serializers = WorkTimeSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WorkTimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkTimeDetail(APIView):
    def get_object(self, pk):
        try:
            return WorkTime.objects.get(pk=pk)
        except WorkTime.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        query = self.get_object(pk)
        serializers = WorkTimeSerializer(query)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        query = self.get_object(pk)
        serializer = WorkTimeSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        query = self.get_object(pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DayDetailApiView(APIView):
    def get(self, request):
        query = DayDetail.objects.all()
        serializers = DayDetailSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DayDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorApointmentsView(APIView):
    def get(self, request, pk):
        query = DayDetail.objects.filter(doctor_id=pk)
        serializers = DayDetailSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)


class DayDetailView(APIView):
    def get_object(self, pk):
        try:
            return DayDetail.objects.get(pk=pk)
        except DayDetail.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        query = self.get_object(pk)
        serializers = DayDetailSerializer(query)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        query = self.get_object(pk)
        serializer = DayDetailSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        query = self.get_object(pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReservedApointmentApiView(APIView):
    def get(self, request):
        query = ReservedApointment.objects.all()
        serializers = ReservedApointmentSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ReservedApointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorReservedView(APIView):
    def get(self, request, pk):
        query = ReservedApointment.objects.filter(doctor_id=pk)
        serializers = ReservedApointmentSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)


class ReservedApointmentDetail(APIView):
    def get_object(self, pk):
        try:
            return ReservedApointment.objects.get(pk=pk)
        except ReservedApointment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        query = self.get_object(pk)
        serializers = ReservedApointmentSerializer(query)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        query = self.get_object(pk)
        serializer = ReservedApointmentSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        query = self.get_object(pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserReservedView(APIView):
    def get(self, request, pk):
        query = ReservedApointment.objects.filter(user_id=pk)
        serializers = ReservedApointmentSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)


def index(request):
    doctors = Doctor.objects.all()
    template = loader.get_template('tabib/index.html')
    args = {'doc': doctors}
    return HttpResponse(template.render(args, request))


class AllDocsView(APIView):
    def get(self, request):
        a = datetime.datetime.now()
        query = Doctor.objects.prefetch_related('worktime', 'daydetail', 'apointments').all()
        serializers = DoctorsSerializer(query, read_only=True, many=True, context={'request': request})
        response = Response(serializers.data, status=status.HTTP_200_OK)
        b = datetime.datetime.now()
        c = b - a
        print('runtime is : ', int(c.total_seconds() * 1000), 'ms')
        return response



