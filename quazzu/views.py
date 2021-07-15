from django.shortcuts import render, redirect
from .forms import LoginForm, UserRegistrationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout


def home(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        form.username = request.POST.get('username', '')
        form.password = request.POST.get('password', '')

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['username'], password=cd['password'])
            if user is None:
                return HttpResponse('Invalid login')

            if not user.is_active:
                return HttpResponse('Disabled account')

            login(request, user)
            return redirect('solutions')
    else:
        form = LoginForm()
    return render(request, 'index.html', {'form': form})



def registration(request):

	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		form.first_name = request.POST.get('first_name', '')
		form.username = request.POST.get('username', '')
		form.last_name = request.POST.get('last_name', '')
		form.email = request.POST.get('email', '')
		form.password = request.POST.get('password', '')
		form.password2 = request.POST.get('password2', '')
		form.company = request.POST.get('company', '')
		form.roles = request.POST.get('roles', '')

		if form.is_valid():
			user = form.save(commit=False)
			# Set the chosen password
			user.set_password(form.cleaned_data['password'])
			# Save User object
			user.save()
			return redirect('home')

	else:
		form = UserRegistrationForm()
	return render(request, 'signup.html', {'form': form})



def solutions(request):

	if request.method == 'POST':
		form = LoginForm(request.POST)
		form.username = request.POST.get('username', '')
		form.password = request.POST.get('password', '')

		if form.is_valid():
		    cd = form.cleaned_data
		    user = authenticate(
		        request, username=cd['username'], password=cd['password'])
		    if user is None:
		        return HttpResponse('Invalid login')

		    if not user.is_active:
		        return HttpResponse('Disabled account')

		    login(request, user)
		    return redirect('home')
	else:
	    form = LoginForm()
	return render(request, 'solutions.html', {'form':form})



def signup_login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        form.username = request.POST.get('username', '')
        form.password = request.POST.get('password', '')

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['username'], password=cd['password'])
            if user is None:
                return HttpResponse('Invalid login')

            if not user.is_active:
                return HttpResponse('Disabled account')

            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'signup.html', {'form': form})