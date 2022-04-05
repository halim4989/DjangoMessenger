# chat/views.py
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.clickjacking import xframe_options_exempt


# @xframe_options_deny
@xframe_options_exempt
def index(request):
    return render(request, 'chat/index.html', {})



@xframe_options_exempt
# @xframe_options_sameorigin
def room(request, room_name):
    # print("************************************")
    # current_user = request.user
    # print(current_user)
    # print(current_user.id)

    # print(request.user)
    # print(request.POST)
    # print("************************************")

    return render(request, 'chat/room.html', {
        'room_name': room_name,     

    })


def room2(request, room_name):

    return render(request, 'chat/room_withStyle_old_edited.html', {
        'room_name': room_name,
    })


