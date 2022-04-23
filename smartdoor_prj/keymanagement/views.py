from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from bootstrap_modal_forms.generic import BSModalUpdateView, BSModalDeleteView
from .forms import LoginForm, KeyModelForm, KeyRegisterForm
from .models import Key


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
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error: Key was not created.")
        return super().form_invalid(form)


class LogView(LoginRequiredMixin, TemplateView):
    template_name = "log.html"


class KeyUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = Key
    template_name = "update.html"
    form_class = KeyModelForm
    success_message = "Success: Key was updated."
    success_url = reverse_lazy("keymanagement:home")


class KeyDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = Key
    template_name = "delete.html"
    success_message = "Success: Key was deleted."
    success_url = reverse_lazy("keymanagement:home")


@login_required
def keys(request):
    data = dict()
    if request.method == "GET":
        keys = Key.objects.all()
        data["table"] = render_to_string("_keys_table.html", {"keys": keys}, request=request)
        return JsonResponse(data)
