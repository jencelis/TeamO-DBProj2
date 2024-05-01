from django.urls import path
from.import views
#from .views import indexPageView
#from .views import listProfView

urlpatterns = [

    path('', views.index, name=''),

]