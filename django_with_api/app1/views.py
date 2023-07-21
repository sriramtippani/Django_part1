from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import authenticate, logout
from django.contrib import messages
from .models import hydjobs, blorejobs, chennaijobs, punejobs
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def homepage_view(request):
    return render(request, 'html/home.html')

@login_required
def hydJobs_view(request):
    job_list = hydjobs.objects.order_by('-date')
    paginator = Paginator(job_list, 10)
    page_number = request.GET.get('page')
    try:
        job_list = paginator.page(page_number)
    except PageNotAnInteger:
        job_list = paginator.page(1)
    except EmptyPage:
        job_list = paginator.page(paginator.num_pages)
    return render(request, 'html/hydjob.html', {'job_list': job_list})


@login_required
def bloreJobs_view(request):
    job_list = blorejobs.objects.order_by('-date')
    paginator = Paginator(job_list, 10)
    page_number = request.GET.get('page')
    try:
        job_list = paginator.page(page_number)
    except PageNotAnInteger:
        job_list = paginator.page(1)
    except EmptyPage:
        job_list = paginator.page(paginator.num_pages)
    return render(request, 'html/blorejobs.html', {'job_list': job_list})


@login_required
def chennaiJobs_view(request):
    job_list = chennaijobs.objects.order_by('-date')
    paginator = Paginator(job_list, 10)
    page_number = request.GET.get('page')
    try:
        job_list = paginator.page(page_number)
    except PageNotAnInteger:
        job_list = paginator.page(1)
    except EmptyPage:
        job_list = paginator.page(paginator.num_pages)
    return render(request, 'html/chennaijobs.html', {'job_list': job_list})


@login_required
def puneJobs_view(request):
    job_list = punejobs.objects.order_by('-date')
    paginator = Paginator(job_list, 10)
    page_number = request.GET.get('page')
    try:
        job_list = paginator.page(page_number)
    except PageNotAnInteger:
        job_list = paginator.page(1)
    except EmptyPage:
        job_list = paginator.page(paginator.num_pages)
    return render(request, 'html/punejobs.html', {'job_list': job_list})


def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(request, 'Registration successful.')

        return homepage_view(request)
        messages.error(request, 'Unsuccessful registration. Invalid information.')
    form = NewUserForm()
    return render(request=request, template_name='html/register.html', context={'register_form': form})



# def login_request(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f'You are now logged in as {username}.')
#                 return homepage_view(request)
#             else:
#                 messages.error(request, 'Invalid username or password.')
#         else:
#             messages.error(request, 'Invalid username or password.')
#     form = AuthenticationForm()
#     return render(request=request, template_name='html/login.html', context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return render(request, 'html/logout.html')
