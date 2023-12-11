from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def homepage(request):
    return render(request , 'home.html')

def register_request(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful")
            # return redirect("login")
        messages.error(request , "Unsccessful registration. Invalid information.")
    return render(request=request, template_name='register.html', context={"register_form":form})