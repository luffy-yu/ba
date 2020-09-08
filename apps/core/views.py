from django.conf import settings
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group as AuthGroup
from django.core import signing
from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic import TemplateView, ListView
from django.views.generic.base import View
from django.views.generic.edit import (FormView, UpdateView, CreateView,
                                       DeleteView)

from .forms import LoginForm, SignupForm
from apps.accounts.models import ElementalUser
from apps.accounts.mixins import UnbannedUserMixin
from apps.projects.models import Project


class Index(UnbannedUserMixin, FormView):
    template_name = 'index.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['featured'] = Project.objects.exclude(featured__isnull=True).order_by('-featured')[:5]
        return context
    
    def form_valid(self, form):
        super(Index, self).form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(self.request, user)
                user.set_ip(self.request)
                if not user.banned:
                    return super(Index, self).form_valid(form)
                else:
                    return redirect(reverse('ban-page'))
            else:
                form.errors['non_field_errors'] = ['Your account is not active.']
                return render(self.request, 'index.html',
                              {'form': form})
        else:
            form.errors['non_field_errors'] = ['Invalid login']
            return render(self.request, 'index.html',
                          {'form': form})


class BanPage(TemplateView):
    template_name = 'banned.html'

    def get(self, request):
        if request.user and not request.user.banned: # if user is logged in and is not banned
            return redirect(reverse('index'))
        else: # user logged and banned
            return render(request, 'banned.html')


class TermsOfService(TemplateView):
    template_name = 'terms_of_service.html'


class SignUp(FormView):
    template_name = 'register.html'
    form_class = SignupForm
    success_url = '/'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('index'))
        return super(SignUp, self).get(request)

    def form_valid(self, form):
        super(SignUp, self).form_valid(form)
        form.save()
        user = authenticate(username=form.cleaned_data.get('username'),
                            password=form.cleaned_data.get('password1'))
        login(self.request, user)
        return redirect(reverse('index'))


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')