from django.conf.urls import url
from .import views

app_name="kindlebizy"
urlpatterns =[
    url(r'^$',views.homeview,name='Homepage'),
    url(r'^about kinder/$',views.popview,name='about'),
    url(r'^order kinder/$',views.order,name='order'),

]