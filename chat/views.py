from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
from chat.models import Thread
# from accounts.models import displayuser


@login_required
def messages_page(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    displayusername=User.objects.all()
    
    context = {
        'Threads': threads,
        'User':displayusername
    }
    return render(request, 'messages.html', context)


def createuser(request):
    alluser=User.objects.all()
    for i in alluser:
        for j in alluser:
            thre= Thread()
            thre.first_person=i.username
            thre.second_person=j.username


