from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


# 1. One-to-One relationship with Django's default User
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ("user", "User"),
        ("admin", "Admin"),
        ("manager", "Manager"),
        ("supervisor", "Supervisor"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )

    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default="user")

    address = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to="user_images/", null=True, blank=True)
    join_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Profile of {self.user.username}"


# 2. ForeignKey relationship: one user can receive many reviews
class UserReview(models.Model):
    reviewed_student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="received_reviews",
    )

    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="written_reviews",
    )

    review_text = models.TextField()

    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    votes = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    comment_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Review by {self.reviewer.username}"


# 3. Many-to-Many relationship: students and subjects
class StudentSubject(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=20, unique=True)
    subject_description = models.TextField(blank=True)
    subject_credits = models.IntegerField(default=0)
    subject_instructor = models.CharField(max_length=100)
    subject_schedule = models.CharField(max_length=100)

    students = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="enrolled_subjects", blank=True
    )

    def __str__(self):
        return f"{self.subject_name} ({self.subject_code})"


# 4. ForeignKey: one student can have multiple certificates
class StudentCertificate(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="certificates"
    )

    certificate_name = models.CharField(max_length=100)
    certificate_number = models.CharField(max_length=50, unique=True)
    certificate_description = models.TextField(blank=True)
    certificate_date = models.DateTimeField(default=timezone.now)

    certificate_file = models.FileField(upload_to="student_certificates/", blank=True)

    def __str__(self):
        return f"{self.certificate_name} - {self.student.username}"
