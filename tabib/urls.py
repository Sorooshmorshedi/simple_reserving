from django.urls import path

from tabib.views import UserApiView, UserDetail, DoctorApiView, DoctorDetail, \
    WorkTimeApiView, WorkTimeDetail, DayDetailApiView, DoctorApointmentsView, UserReservedView, \
    DayDetailView, ReservedApointmentApiView, ReservedApointmentDetail, DoctorReservedView, index, AllDocsView

urlpatterns = [
    path('', index, name='index'),
    path('user/', UserApiView.as_view(), name='UserApi'),
    path('user/<int:pk>/', UserDetail.as_view(), name='userDetail'),
    path('doctor/', DoctorApiView.as_view(), name='doctorApi'),
    path('doctor/<int:pk>/', DoctorDetail.as_view(), name='doctorDetail'),
    path('worktime/', WorkTimeApiView.as_view(), name='workTime'),
    path('worktime/<int:pk>/', WorkTimeDetail.as_view(), name='workTimeDetail'),
    path('daydetail/', DayDetailApiView.as_view(), name='dayDetailApi'),
    path('daydetail/<int:pk>/', DayDetailView.as_view(), name='dayDetail'),
    path('docdaydetail/<int:pk>/', DoctorApointmentsView.as_view(), name='docdaydetail'),
    path('apointments/', ReservedApointmentApiView.as_view(), name='reservedApointmentApi'),
    path('apointments/<int:pk>/', ReservedApointmentDetail.as_view(), name='apointments'),
    path('doc/reserved/<int:pk>/', DoctorReservedView.as_view(), name='doctorReservedApi'),
    path('user/reserved/<int:pk>/', UserReservedView.as_view(), name='userReservedApi'),
    path('doc/all/', AllDocsView.as_view(), name='alldocapi'),

]
