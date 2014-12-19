from django.shortcuts import render, Http404, render_to_response, RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm


def home(request):
    users = User.objects.filter(is_active=True)
    context = {'users': users}
    return render(request, 'home.html', context)


def single_user(request, username):
    try:
        user = User.objects.get(username=username)
        if user.is_active:
            single_user = user
    except:
        raise Http404

    context = {'single_user': user}
    return render(request, 'profiles/single_user.html', context)


@login_required
def edit_profile(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    user_profile_form = UserProfileForm(request.POST or None, request.FILES or None, instance=user_profile)
    if user_profile_form.is_valid():
        form = user_profile_form.save(commit=False)
        form.save()
    return render_to_response('profiles/edit_profile.html', locals(), context_instance=RequestContext(request))