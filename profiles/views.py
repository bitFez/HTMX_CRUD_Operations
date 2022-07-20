from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from. forms import UserEditForm, CeremonyForm
from .models import UserProfile, Ceremonies
# Create your views here.

@login_required(login_url='accounts/login')
def home(request):
    user = get_object_or_404(UserProfile, pk=request.user.pk)
    if request.method == 'GET':
            
        form = CeremonyForm()
        
        def days_until(date):
            delta = datetime.date(date) - datetime.now().date()
            return delta.days
        d1 = user.subs_end_date
        days = days_until(d1)
        
        context = {'user': user, 'days':days, 'form':form}
        return render(request, 'profiles/home.html', context)
    elif request.method == 'POST':
        form = CeremonyForm(request.POST)
        if form.is_valid:
            user = form.save()
            return HttpResponse("Hi")
        context = {'user': user, 'days':days, 'form':form}
        return render(request, 'profiles/home.html', context)


@login_required(login_url='accounts/login')
def cerListView(request):
    form = CeremonyForm()
    user = get_object_or_404(UserProfile, pk=request.user.pk)
    cerList = Ceremonies.objects.filter(user=request.user)[0:7]
    
    context = {'user': user, 'cerList':cerList, 'form':form}
    return render(request, 'profiles/ceremonies_listview.html', context)


def daily_checkin(request):
    user = get_object_or_404(UserProfile, request.user)

    context = {'user': user,}
    return render(request, 'profiles/dashboard.html', context)


@login_required
def add_ceremony(request):
    user = get_object_or_404(UserProfile, pk=request.user.pk)
    
    if request.method == 'POST':
        form = CeremonyForm(request.POST)

        if form.is_valid():
            form.save(commit=False)
            form.user = request.user.id
            form.save()
            return redirect('profiles:cerlistview') #return HttpResponseRedirect(reverse(''))
        else:
            form = CeremonyForm(instance=request.user)
        context = {
            'user':user, 
            'form':form,
            }
    return render(request, 'profiles/ceremonies_listview.html', context)


def profile_detail(request, pk):
    #
    #
    user = get_object_or_404(UserProfile, pk=pk)
        
    # articles = Articles.objects.filter(bookmarked=profile.id)
    # questions = Questions.objects.filter(author=user.id)
    
    points = user.rank
    rank = user.rank # karma - xp
    
    context = {'user':user, 'points':points,'rank':rank} # , 'image_url':image_url
    return render(request, 'profiles/student_detail.html', context)

@login_required
def edit_profile(request):
    user = get_object_or_404(UserProfile, pk=request.user.pk)
    
    points = user.rank
    rank = user.rank # karma - xp
    
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST or None, instance=request.user)
    
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('profiles:edit_profile'))
    else:
        user_form = UserEditForm(instance=request.user)
    context = {
        'user':user, 
        'points':points,
        'rank':rank,
        'user_form':user_form,
        }
    return render(request, 'profiles/edit_profile.html', context)