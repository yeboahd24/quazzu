from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegistrationForm

# Register your models here.

class UserProfileAdmin(UserAdmin):
	add_form = UserRegistrationForm
	model = User
	can_delete = True
	list_display = ['username', 'email']
	verbose_name_plural = 'Users'

admin.site.register(User, UserProfileAdmin)
