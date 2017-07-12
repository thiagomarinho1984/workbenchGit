from django.conf.urls import url

from . import views
from . import workbench

urlpatterns = [
    #index
    url(r'^$', views.index, name='index'),

]