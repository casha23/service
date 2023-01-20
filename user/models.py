from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import RegexValidator
from django.db import models


class CustomUserManager(UserManager):
    def create_user(self, phone_number, email, password=None):
        """
        Creates and saves a User with the given phonen umber, email and password.
        """
        if not phone_number:
            raise ValueError('Users must phone number')

        user = self.model(
            phone_number=phone_number,
            email=email
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email, password):
        """
        Creates and saves a superuser with the given phonen umber, email and password.
        """
        user = self.create_user(
            phone_number=phone_number,
            email=email,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    phone_regex = RegexValidator(
        regex=r'^\+380\d{9}$', message="Phone number must be entered in the format: '+380xxxxxxxxx'"
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=True, unique=True)
    username = models.CharField(max_length=150, unique=False, default='', blank=True, null=True)
    is_master = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'

    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number
