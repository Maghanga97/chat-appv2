from pyexpat.errors import messages
from unicodedata import name
from django.shortcuts import render, redirect
from .models import ChatRoom, Messages
from django.contrib.auth.models import User
from django.http import JsonResponse
# Create your views here.
def home(request):
    return render(request, 'chat/home.html', {})

def create_room(request):
    room = request.POST.get('chatroom')
    user_name = request.POST.get('username')
    try:
        user = User.objects.get(username=user_name)
    except:
        user = User.objects.create(username=user_name)
        user.save()

    if ChatRoom.objects.filter(name=room).exists():
        return redirect('/chat/'+room+'/?username='+user_name)

    else:
        print('The if block did not run...')
        chatroom = ChatRoom.objects.create(name=room)
        chatroom.save()
        return redirect('/chat/'+room+'/?username='+user_name)

def room(request, room):
    chatroom = ChatRoom.objects.get(name=room)
    messages = Messages.objects.filter(room=chatroom)
    user_name = request.GET.get('username')
    user = User.objects.get(username=user_name)
    return render(request, 'chat/room.html', {'room':chatroom, 'user':user, 'msgs':messages})


def send_message(request):
    room = request.POST['room']
    user = request.POST['user']
    message = request.POST['message']
    chatroom = ChatRoom.objects.get(name=room)
    user = User.objects.get(username=user)
    message = Messages.objects.create(text_msg=message,user=user,room=chatroom)
    message.save()
    return redirect('/chat/'+room+'/?username='+user)


def getMessages(request, room):
    chatroom = ChatRoom.objects.get(name=room)
    messages = Messages.objects.filter(room=chatroom)

    data = []
    for msg in messages:
        msg_dict = {'text_msg': msg.text_msg, 'user': msg.user.username, 'time': msg.time_stamp}
        data.append(msg_dict)
        
    return JsonResponse({"messages": data})
