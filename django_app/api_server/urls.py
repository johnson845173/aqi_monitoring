from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	# path('task-list/', views.taskList, name="task-list"),
	path('test/', views.taskDetail, name="task-detail"),
	path('task-create/', views.taskCreate, name="task-create"),
	# path('create/<str:data>/', views.create, name="create"),
	
	path('task-update/<str:data>/', views.taskUpdate, name="task-update"),
	path('delete/', views.taskDelete, name="delete"),
	path('create/', views.create, name="create"),
    
	path('student-list/', views.student_list, name="student_list"),
	path('add-attendance/', views.add_attendence, name="student_list"),
	path('get-attendance-by-usn/', views.get_attendance_by_usn, name="usn"),
	path('get-attendance-by-date/', views.get_attendance_by_date, name="date"),

	path('today-weather/', views.get_today_weather, name="get_today_weather"),
	path('get-weather/', views.getdata, name="getdata"),
    path('add_weather/',views.add_iot_weather,name="Add weather"),
	path('verify/', views.verify, name="verify"),
]
