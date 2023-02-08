from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, ProfileUpdateForm, UserUpdateForm
from .models import Profile

def register(request):

    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user =user_form.save(commit=False)
            new_user.save()
            Profile.objects.create(user=new_user)
            username = new_user.cleaned_data.get('username')
            messages.success(request, f'{username} has been created')
            return redirect('profile')
    else:
        user_form = RegisterForm()
        messages.error(request, "Incorrect!.")

    return render(request, 'account/register.html', {'user_form':user_form})

@login_required
def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(instance=request.user,
                                data=request.POST)
        p_form = ProfileUpdateForm(instance=request.user.profile,
                                   data=request.POST,
                                   files=request.FILES)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'account/profile.html', {'u_form':u_form, 'p_form':p_form})


@login_required
def dashboard(request):

    return render(request, 'account/dashboard.html', {'section':'dashboard'})
