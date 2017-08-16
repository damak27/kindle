from django.conf.urls import url
from .import views

app_name="kindlebizy"
urlpatterns =[
    url(r'^$',views.homeview,name='Homepage'),
    url(r'^$',views.popview,name='pop'),

]