from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "chat/index.html")

def chatter(request):
    ctx = {"message": "Test message from chatter view"}
    return render(request, "chat/chatter.html", context=ctx)