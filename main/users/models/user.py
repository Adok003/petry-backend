from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email обязателен")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff"):
            raise ValueError("Суперпользователь должен иметь is_staff=True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Суперпользователь должен иметь is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    REGION_CHOICES = [
        ('Almaty', 'Алматы'),
        ('Astana', 'Астана'),
        ('Shymkent', 'Шымкент'),
        ('Akmola', 'Акмолинская'),
        ('Aktobe', 'Актюбинская'),
        ('AlmatyRegion', 'Алматинская'),
        ('Atyrau', 'Атырауская'),
        ('EastKazakhstan', 'Восточно-Казахстанская'),
        ('Zhambyl', 'Жамбылская'),
        ('WestKazakhstan', 'Западно-Казахстанская'),
        ('Karaganda', 'Карагандинская'),
        ('Kostanay', 'Костанайская'),
        ('Kyzylorda', 'Кызылординская'),
        ('Mangystau', 'Мангистауская'),
        ('Pavlodar', 'Павлодарская'),
        ('NorthKazakhstan', 'Северо-Казахстанская'),
        ('Turkestan', 'Туркестанская'),
        ('Ulytau', 'Улытауская'),
    ]

    username = None
    email = models.EmailField(unique=True)

    position = models.CharField(max_length=100, blank=True, default='')
    head = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subordinates')
    role = models.ForeignKey('users.Role', on_delete=models.SET_NULL, null=True, blank=True)
    region = models.CharField(choices=REGION_CHOICES, max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, default='active')
    payment_type = models.CharField(max_length=50, blank=True, default='')
    payment_period = models.CharField(max_length=50, blank=True, default='')
    reset_code = models.CharField(max_length=10, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Role(models.Model):
    ROLE_CHOICES = [
        ('superadmin', 'Супер Админ'),
        ('executor', 'Частный Судоисполнитель'),
        ('assistant', 'Помощник ЧСИ'),
    ]
    name = models.CharField(max_length=20, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.name
