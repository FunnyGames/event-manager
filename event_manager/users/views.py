from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .forms import UserRegisterForm, ResetPasswordForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .email import sendResetPasswordEmail

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account {username} has been created! Now you can log in')
            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
@permission_required('is_superuser')
def users(request):
    page = request.GET.get('page')
    limit = request.GET.get('limit')
    if limit == None:
        limit = 5
    else:
        limit = int(limit)
        if limit < 1 or limit > 20:
            limit = 5

    p = Paginator(User.objects.all(), limit)
    if page == None:
        page = 1
    else:
        page = int(page)
        if page < 1 or page > p.num_pages:
            page = 1
    context = {
        'page_obj': p.get_page(page)
    }
    return render(request, 'users/users_list.html', context)


def resetPassword(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            sendResetPasswordEmail(email)
            messages.success(
                request, f'Successfully sent email to {email} with instructions')
            return redirect('login')
    else:
        form = ResetPasswordForm()
    context = {
        'form': form
    }
    return render(request, 'users/reset.html', context)
