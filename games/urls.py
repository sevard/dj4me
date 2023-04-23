from django.urls import path

from . import views


appname = 'games'

urlpatterns = [
    path("", views.index, name="games-index"),
]
