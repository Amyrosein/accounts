from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager


class User(AbstractBaseUser):
	email = models.EmailField(
		verbose_name="آدرس ایمیل",
		max_length=255,
		unique=True,
	)
	is_active = models.BooleanField(default=True, verbose_name="فعال است ؟")
	is_admin = models.BooleanField(default=False, verbose_name="ادمین است ؟")

	objects = UserManager()

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = []

	class Meta:
		verbose_name = "کاربر"
		verbose_name_plural = "کاربر ها"

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

	@property
	def is_staff(self):
		"Is the user a member of staff?"
		# Simplest possible answer: All admins are staff
		return self.is_admin
