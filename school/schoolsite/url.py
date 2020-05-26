from django.conf.urls import url
from schoolsite import views
from schoolsite import signinviews

urlpatterns = [
    url('',views.index,name='index'),
]
