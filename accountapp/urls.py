from django.urls import path

from accountapp.views import hello_world

app_names = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
]