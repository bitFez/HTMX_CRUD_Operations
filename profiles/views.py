from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from. forms import UserEditForm
from .models import UserProfile
# Create your views here.
def home(request):
    user = get_object_or_404(UserProfile, pk=request.user.pk)
    def days_until(date):
        delta = datetime.date(date) - datetime.now().date()
        return delta.days
    d1 = user.subs_end_date
    days = days_until(d1)
        
    context = {'user': user, 'days':days}
    return render(request, 'profiles/home.html', context)

def daily_checkin(request):
    user = get_object_or_404(UserProfile, request.user)

    context = {'user': user,}
    return render(request, 'profiles/dashboard.html', context)


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