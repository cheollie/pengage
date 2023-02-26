from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from .forms import CreateUserForm, EditProfileForm  # import custom user creation form

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

# edit user profile
# update user profile
def update(request):
    if not request.user.is_authenticated:
        raise Http404("You are not logged in")
    editForm = EditProfileForm(instance=request.user)
    user = request.user
    if request.method == 'POST':
        editForm = EditProfileForm(request.POST, instance=request.user)
        if editForm.is_valid():
            editForm.save()
        return HttpResponseRedirect('/user/')

    return render(request, 'home/update.html', {'user': user, 'form': editForm})
