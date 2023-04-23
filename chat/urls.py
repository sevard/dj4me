from django.urls import path

from . import views


appname = "chat"

urlpatterns = [
    path("", views.index, name="chat-intex")
]
