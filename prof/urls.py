from django.urls import path
from.import views
#from .views import indexPageView
#from .views import listProfView

urlpatterns = [

    path('', views.BootstrapFilterView, name='prof/'),
    path('list/', views.index, name='index'),

]