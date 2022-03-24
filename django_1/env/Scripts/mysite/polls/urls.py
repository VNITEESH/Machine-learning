from django.urls import path
from polls import views

urlpatterns = [
    path("", views.index, name="index"),
    path("name",views.name,name="name"),
    path("time",views.time,name="time")
]