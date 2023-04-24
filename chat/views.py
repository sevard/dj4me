from django.shortcuts import render
from dj4me_project.settings import OAI_API_KEY
import json
import requests
# Create your views here.


def send_text_message(message):
    headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer {OAI_API_KEY}', }
    payload = json.dumps({
        "model": "text-davinci-003",
        "prompt": message
    })
    r = requests.post('https://api.openai.com/v1/completions',
                      headers=headers, data=payload)

    response_content_dict = json.loads(r.content)
    response_text = response_content_dict.get('choices')[0].get('text')
    return response_text.strip()


def send_chat_message(message):
    headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer {OAI_API_KEY}', }
    payload = json.dumps({
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": message, "name": "serg"}]
    })
    r = requests.post('https://api.openai.com/v1/chat/completions',
                      headers=headers, data=(payload))

    resp_content_di = json.loads(r.content)
    content = resp_content_di.get('choices')[0].get('message').get('content')
    return content


def index(request):
    return render(request, "chat/index.html")


def chatter(request):
    if not request.POST.get('user_message'):
        ctx = {"message_response": "Please enter your message!"}
    else:
        msg = request.POST.get('user_message')
        msg_response = send_chat_message(msg)
        ctx = {"message_response": msg_response}
    return render(request, "chat/chatter.html", context=ctx)
