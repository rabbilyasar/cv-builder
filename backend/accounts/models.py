from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    postcode = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    country = models.CharField(max_length=250, null=True, blank=True)
    country_code = models.CharField(max_length=3, null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)
    marital_status = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    nacionality = models.CharField(max_length=50, null=True, blank=True)
    military_service = models.BooleanField(default=False, null=True, blank=True)
    driving_license = models.BooleanField(default=False, null=True, blank=True)
    job_title = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateField(auto_now=True, null=True, blank=True)
