from django.db import models
from django.contrib.auth.models import AbstractUser


ROLES = (

	('Professional Developer', 'Professional Developer'),
	('Hobbyist', 'Hobbyist'),
	('Student', 'Student'),
	('Manager', 'Manager'),
	('Other', 'Other')

	)


class User(AbstractUser):
	company = models.CharField(max_length=100, blank=True)
	roles =models.CharField(max_length=100, choices=ROLES, blank=True)


	def __str__(self):
		return self.first_name