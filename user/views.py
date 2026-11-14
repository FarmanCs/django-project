from django.shortcuts import render

from .models import UserProfile, UserReview, StudentSubject, StudentCertificate


# Create your views here.
def userindex(request):
    users = UserProfile.objects.all()
    return render(request, "user.html", {"users": users})
