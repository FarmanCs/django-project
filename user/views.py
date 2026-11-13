from django.shortcuts import render

from .models import User


# Create your views here.
def userindex(request):
    users = User.objects.all()
    return render(request, "user.html", {"users": users})
