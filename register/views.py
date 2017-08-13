from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required #login  def
from django.contrib.auth.mixins import LoginRequiredMixin #login  viw 
from django.contrib import messages 
from django.http import HttpResponse
from django.views.generic import CreateView # registration
from django.contrib.auth import get_user_model #registration
from .forms import RegisterForm
from django.http import HttpResponseRedirect

User = get_user_model()

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'apli/register.html'
    success_url = "/apli/index_contact"