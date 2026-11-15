from django.shortcuts import render

from .models import (
    UserProfile,
    UserReview,
    StudentSubject,
    StudentCertificate,
)

from .form import SubjectForm


def userindex(request):
    users = UserProfile.objects.select_related("user").all()

    return render(
        request,
        "user.html",
        {"users": users},
    )


def user_subject(request):

    # Default: empty QuerySet
    subjects = StudentSubject.objects.none()

    if request.method == "POST":

        form = SubjectForm(request.POST)

        if form.is_valid():

            # Returns a UserProfile object
            selected_profile = form.cleaned_data["user_subject"]

            # Get subjects associated with the selected profile's User
            subjects = StudentSubject.objects.filter(students=selected_profile.user)

    else:
        form = SubjectForm()

    return render(
        request,
        "subject.html",
        {
            "subject": subjects,
            "form": form,
        },
    )
