from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import UserProfile, UserReview, StudentSubject, StudentCertificate


# Display profile inside the default Django User page
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    extra = 0
    max_num = 1


# Extend Django's default User admin
class CustomUserAdmin(UserAdmin):
    inlines = [UserProfileInline]


# Unregister the original admin registration
admin.site.unregister(User)

# Register the default User with our inline profile
admin.site.register(User, CustomUserAdmin)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "phone_number", "join_date")

    search_fields = ("user__username", "user__email", "phone_number")

    list_filter = ("role",)


@admin.register(UserReview)
class UserReviewAdmin(admin.ModelAdmin):
    list_display = ("reviewed_student", "reviewer", "rating", "comment_date")

    search_fields = ("reviewed_student__username", "reviewer__username", "review_text")

    list_filter = ("rating", "comment_date")


@admin.register(StudentSubject)
class StudentSubjectAdmin(admin.ModelAdmin):
    list_display = (
        "subject_name",
        "subject_code",
        "subject_credits",
        "subject_instructor",
    )

    search_fields = ("subject_name", "subject_code", "subject_instructor")

    filter_horizontal = ("students",)


@admin.register(StudentCertificate)
class StudentCertificateAdmin(admin.ModelAdmin):
    list_display = (
        "certificate_name",
        "student",
        "certificate_number",
        "certificate_date",
    )

    search_fields = ("certificate_name", "student__username", "certificate_number")
