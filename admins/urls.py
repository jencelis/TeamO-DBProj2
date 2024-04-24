from django.urls import path
from.import views

urlpatterns = [
    path("", views.home, name="home")
]

from .views import salary_report

urlpatterns = [
    path('salary-report/', salary_report, name='salary_report'),
]