from django.urls import path
from . import views

urlpatterns = [
    path("", views.admin_home, name="admin_home"),
    path('salary-report/', views.salary_report, name='salary_report'),
    path('performance/', views.performance_request, name='performance_form'),
]