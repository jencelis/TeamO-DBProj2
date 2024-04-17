from django.urls import path
from.import views
#from .views import indexPageView
from .views import listProfView

urlpatterns = [
    #path("", indexPageView, name="index"),
    #path("listprofs", listProfView, name="Instructors"),
    path("", views.listProfView, name="Instructors")
]