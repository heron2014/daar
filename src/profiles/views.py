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


# @login_required
# def edit_profile(request):
#
#     # user_profile = UserProfile.objects.get(user=request.user)
#     user_profile_form = UserProfileForm(request.POST or None, request.FILES or None, instance=request.user)
#     if user_profile_form.is_valid():
#         form = user_profile_form.save(commit=False)
#         form.save()
#     return render_to_response('profiles/edit_profile.html', locals(), context_instance=RequestContext(request))

@login_required
def edit_profile(request):

    try:
        p = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        p = None
    user_profile_form = UserProfileForm(request.POST, request.FILES, instance=p)

    if user_profile_form.is_valid():
        form = user_profile_form.save(commit=False)
        form.save()
    else:
        user_profile_form = UserProfileForm()

    return render(request, 'profiles/edit_profile.html', {'user_profile_form': user_profile_form,
                                                               })