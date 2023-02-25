from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .forms import CreateUserForm  # import custom user creation form

# display home page
def index(request):
    return render(request, 'home/index.html')

# display register page
def register(request):
    userForm = CreateUserForm()
    if request.method == 'POST':
        userForm = CreateUserForm(request.POST)
        if userForm.is_valid():
            userForm.save()
            return redirect('/')
    return render(request, 'home/register.html', {'form': userForm})


# display login page
def login(request):
    return render(request, 'home/login.html')

# display logout page
def logout(request):
    return render(request, 'home/logout.html')
