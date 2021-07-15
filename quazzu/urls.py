from django.urls import path

from .views import home, registration, solutions, signup_login

urlpatterns = [
	path('', home, name='home'),
	path('registration/', registration, name="signup"),
	path('solutions/', solutions, name="solutions"),
	path('signup_login/', signup_login, name="signup_login")

]