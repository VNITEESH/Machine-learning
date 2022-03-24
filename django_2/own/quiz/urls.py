from django.urls import path
from quiz import views
urlpatterns=[
    path('',views.intro,name='intro'),
    path('intro',views.intro2,name='intro2'),
]