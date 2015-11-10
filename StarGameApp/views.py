from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from models import *
# Create your views here.


class LoginView(View):
    template = "login.html"

    def post(self, request):
        user_name = request.POST.get("user", None)
        user_pass = request.POST.get("pass", None)
        user = authenticate(username=user_name, password=user_pass)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/principal")
            else:
                #Usuario no activo
                pass
        else:
            #Usuario no existe
            pass
        return render(request, self.template, {})

    def get(self, request):
        try:
            profile = UserProfile.objects.get(user=request.user)
            return redirect("/principal")
        except Exception:
            return render(request, self.template, {})

@login_required
def user_logout(request):
    request.session.flush()
    logout(request)
    return HttpResponseRedirect('/login')

@login_required
def principalView(request):
    profile = UserProfile.objects.get(user=request.user)
    context = {
        "panel": "principal",
        "profile": profile,
    }
    return render(request, "home.html", context)

@login_required
def edificiosView(request):
    profile = UserProfile.objects.get(user=request.user)
    buildings = Building.objects.filter(race=profile.race, thematic=profile.thematic)
    context = {
        "panel": "edificios",
        "buildings": buildings,
    }
    return render(request, "home.html", context)

@login_required
def unidadesView(request):
    profile = UserProfile.objects.get(user=request.user)
    units = Unit.objects.filter(race=profile.race, thematic=profile.thematic)
    context = {
        "panel": "unidades",
        "units": units,
    }
    return render(request, "home.html", context)

@login_required
def tecnologiasView(request):
    profile = UserProfile.objects.get(user=request.user)
    general_technologies = GeneralTechnology.objects.filter(thematic=profile.thematic)
    context = {
        "panel": "tecnologias",
        "general_tech": general_technologies,
    }
    return render(request, "home.html", context)

@login_required
def datosCuentaView(request):
    context = {
        "panel": "datosCuenta",
    }
    return render(request, "home.html", context)

