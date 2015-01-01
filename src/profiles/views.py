from django.shortcuts import render, Http404, render_to_response, RequestContext, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
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
    # u = User.objects.get(username=user)
    try:
        u_p = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        u_p = UserProfile.objects.create(user=user)
    except:
        u_p = None
    user_profile_form = UserProfileForm(request.POST or None, request.FILES or None, instance=u_p)
    if user_profile_form.is_valid():
        u_p_form = user_profile_form.save(commit=False)
        u_p_form.user = request.user
        u_p_form.save()
        return HttpResponseRedirect('/')
    else:
        user_profile_form = UserProfileForm()

    return render(request, 'profiles/edit_profile.html', {'user_profile_form': user_profile_form,
                                                       })

# @login_required
# def edit_profile(request):
#
#     # user_profile = UserProfile.objects.get(user=request.user)
#     user_profile_form = UserProfileForm(request.POST or None, request.FILES or None, instance=request.user)
#     if user_profile_form.is_valid():
#         form = user_profile_form.save(commit=False)
#         form.save()
#     return render_to_response('profiles/edit_profile.html', locals(), context_instance=RequestContext(request))

# @login_required
# def edit_profile(request):
#     user = request.user
#     # try:
#     #     p = UserProfile.objects.get(user=request.user)
#     # except UserProfile.DoesNotExist:
#     #     p = None
#     user_profile_inst = get_object_or_404(UserProfile, user=user)
#
#     user_profile_form = UserProfileForm(request.POST or None, request.FILES or None, instance=user_profile_inst)
#
#     if user_profile_form.is_valid():
#         form = user_profile_form.save(commit=False)
#         form.user = request.user
#         form.save()
#     else:
#         user_profile_form = UserProfileForm()
#
#     return render(request, 'profiles/edit_profile.html', {'user_profile_form': user_profile_form,
#                                                            })


