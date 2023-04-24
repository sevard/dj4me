from django.urls import path

from . import views


app_name = "chat"

urlpatterns = [
    # ex: 127.0.0.1/chat/
    path("", views.index, name="chat-index"),
    # ex: 127.0.0.1/chat/chatter
    path("chatter", views.chatter, name="chatter")
]
