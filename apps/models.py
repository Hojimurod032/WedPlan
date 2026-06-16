from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateTimeField, Model, TextField, ForeignKey, CASCADE, TextChoices, DecimalField, \
    DateField, ImageField


class CustomUserManager(BaseUserManager):
    def _create_user(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError("Phone number kiritilishi shart")

        user = self.model(phone_number=phone_number, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser uchun is_staff=True bo‘lishi kerak")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser uchun is_superuser=True bo‘lishi kerak")

        return self._create_user(phone_number, password, **extra_fields)


class User(AbstractUser):
    username = None
    phone_number = CharField(max_length=20, unique=True)
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    tg_username = CharField(max_length=255)
    created_at = DateTimeField(auto_now_add=True)


class Guest(Model):
    class StatusType(TextChoices):
        SUCCESS = 'success', 'Keladi'
        INVITED = 'invited', 'Taklif qilindi'
        NOT_COMING = 'unsuccess', 'Kemidi'

    full_name = CharField(max_length=100)
    phone_number = CharField(max_length=20)
    tg_username = CharField(max_length=50)
    status = CharField(max_length=55, choices=StatusType.choices, default=StatusType.INVITED)
    food = CharField(max_length=100)
    group = CharField(max_length=200)
    notes = TextField()


class BudgetItems(Model):
    category = CharField(max_length=50)
    plan_price = DecimalField(max_digits=17, decimal_places=2)
    success_price = DecimalField(max_digits=17, decimal_places=2)
    notes = TextField()


class Task(Model):
    class StatusType(TextChoices):
        SUCCESS = 'success', 'Bajarildi'
        NOT_COMING = 'unsuccess', 'Bajarilmadi'

    title = CharField(max_length=50)
    term = DateTimeField(auto_now_add=True)
    status = CharField(max_length=55, choices=StatusType.choices)


class Vendor(Model):
    category = CharField(max_length=50)
    name = CharField(max_length=100)
    city = CharField(max_length=100)
    adress = CharField(max_length=100)
    avg_cost = DecimalField(max_digits=17, decimal_places=2)
    contact = CharField(max_length=20)
    rate = DecimalField(max_digits=5, decimal_places=0, default=0)
    photo = ImageField(upload_to='vendor_img/')


class Review(Model):
    vendor = ForeignKey(Vendor, on_delete=CASCADE)
    user = ForeignKey(User, on_delete=CASCADE)
    rate = DecimalField(max_digits=5, decimal_places=0, default=0)
    comment = TextField()
    created_at = DateTimeField(auto_now_add=True)


class Invite(Model):
    couple = CharField(max_length=50)
    wedding_date = DateTimeField(auto_now_add=True)
    location = CharField(max_length=50)
    notes = TextField()
