from django.shortcuts import render

def user_profile(request):
    context = {

    }
    return render(request, template_name="profile.html", context={})

def create_post(request):
    return render(request, template_name= "profile.html", context={})