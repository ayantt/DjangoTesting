from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import User, Location


def user(request):
    all_user = User.objects.all()
    all_location = Location.objects.all()
    context = {
        'all_user': all_user,
        'all_location': all_location,
    }
    return render(request, 'userProfile/user.html', context)


def details(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'userProfile/info.html', {'user': user})


def addUser(request):
    context = {}
    return render(request, 'userProfile/addUser.html', context)


def hello(request):
    context = {}
    return render(request, 'userProfile/home.html', context)


class UserView(generic.ListView):
    template_name = 'userProfile/user.html'
    def get_queryset(self):
        return User.objects.all()



