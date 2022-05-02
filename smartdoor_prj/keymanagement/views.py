import os
import logging
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from bootstrap_modal_forms.generic import BSModalUpdateView, BSModalDeleteView
from django.conf import settings
from .forms import LoginForm, KeyModelForm, KeyRegisterForm
from .models import Key

# path to root directory
BASE_DIR = getattr(settings, "BASE_DIR", None)

logger = logging.getLogger(__name__)


class Login(LoginView):
    form_class = LoginForm
    template_name = "login.html"


class HomeView(LoginRequiredMixin, ListView):
    model = Key
    context_object_name = "keys"
    template_name = "home.html"


class RegisterView(LoginRequiredMixin, CreateView):
    model = Key
    template_name = "register.html"
    form_class = KeyRegisterForm
    success_url = reverse_lazy("keymanagement:home")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Success: Key was created.")
        logger.info(f"{form.cleaned_data['name']}'s {form.cleaned_data['device']} is registered.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error: Key was not created.")
        return super().form_invalid(form)


class LogView(LoginRequiredMixin, TemplateView):
    template_name = "log.html"

    def get_context_data(self):
        context = super().get_context_data()
        with open(os.path.join(BASE_DIR, "logs", "django.log"), "r", encoding="utf-8") as f:
            context["log_text"] = f.read()
        return context


class KeyUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = Key
    template_name = "update.html"
    form_class = KeyModelForm
    success_message = "Success: Key was updated."
    success_url = reverse_lazy("keymanagement:home")

    def form_valid(self, form):
        logger.info(f"{form.cleaned_data['name']}'s {form.cleaned_data['device']} is updated.")
        return super().form_valid(form)


class KeyDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = Key
    template_name = "delete.html"
    success_message = "Success: Key was deleted."
    success_url = reverse_lazy("keymanagement:home")

    def delete(self, request, *args, **kwargs):
        object = self.get_object()
        logger.info(f"{object.name}'s {object.device} is deleted.")
        return super().delete(request, *args, **kwargs)


@login_required
def keys(request):
    data = dict()
    if request.method == "GET":
        keys = Key.objects.all()
        data["table"] = render_to_string("_keys_table.html", {"keys": keys}, request=request)
        return JsonResponse(data)
