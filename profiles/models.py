from tabnanny import verbose
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as gtl
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from datetime import date
from django.urls import reverse

# Customer user manager is used to create an extended user profile other than the standard one Django has built in
class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(gtl('You must provide an email address'))

        if not user_name:
            raise ValueError(gtl('You must provide a user name address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    #user = models.ModelOneToOneField(User, related_name="user_profile", on_delete=models.CASCADE)
    email = models.EmailField(gtl('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    start_date = models.DateTimeField(default=timezone.now)
    date_extended = models.DateTimeField(blank=True, null=True)
    subs_end_date = models.DateTimeField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    has_psm1 = models.BooleanField(default=False)
    has_psm2 = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/profile_pics', null=True, blank=True, default="images/avatar.png", help_text=gtl('Choose your avatar'), verbose_name=gtl('Profile Picture'))
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']
    
    def __str__(self):
        return self.user_name

    def get_absolute_url(self):
        return reverse("profiles:profile_detail", kwargs={'id':self.id})

CEREMONY_TYPES = (
        ('DS', 'Daily Scrum'),
        ('SP', 'Sprint Planning'),
        ('SR', 'Sprint Review'),
        ('SRET', 'Sprint Retrospective'),
        ('BLR', 'Backlog Refinement'),
    )

class CeremonyChoices(models.Model):
    ceremony = models.CharField(max_length=300)
    has_facilitated = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Ceremony Choice"
        verbose_name_plural = "Ceremony Choices"

    def __str__(self):
        return self.ceremony

class Ceremonies(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    cer_date = models.DateTimeField(blank=True)
    ceremonies = models.ManyToManyField(CeremonyChoices)
    
    class Meta:
        ordering = ["-cer_date"]
        verbose_name = "Ceremony"
        verbose_name_plural = "Ceremonies"

    def __str__(self):
        return f"{self.user.first_name} - {self.cer_date}"
    
