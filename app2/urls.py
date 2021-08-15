from app2.views import kumar
from django.urls import path
from app2.views import *
app_name='app2'
urlpatterns=[
       path('kumar/',kumar,name='kumar'),
]