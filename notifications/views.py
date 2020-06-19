from django.contrib.auth import login, logout
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from notifications.forms import PushForm, OptionForm, UserLoginForm
from notifications.mixin import CustomLoginRequiredMixin
from notifications.models import Push, Option


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('push_list')
    else:
        if request.user.is_authenticated:
            return redirect('push_list')
        else:
            form = UserLoginForm()
    return render(request, 'notifications/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login_user')


class PushListView(CustomLoginRequiredMixin, ListView):
    model = Push
    context_object_name = 'pushes'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Список пуш уведомлений'
        return ctx

    def get_queryset(self):
        return Push.objects.filter(is_deleted=False)


class PushDetailView(CustomLoginRequiredMixin, DetailView):
    model = Push

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Просмотр пуш уведомления'
        return ctx

    def get_object(self, queryset=None):
        _id = self.kwargs.get('pk')
        return get_object_or_404(Push, id=_id)


class PushCreateView(CustomLoginRequiredMixin, CreateView):
    form_class = PushForm
    template_name = 'notifications/push_create.html'
    success_url = '/pushes/'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Создание пуш уведомления'
        return ctx


class PushUpdateView(CustomLoginRequiredMixin, UpdateView):
    form_class = PushForm
    template_name = 'notifications/push_create.html'

    def get_object(self, queryset=None):
        _id = self.kwargs.get('pk')
        return get_object_or_404(Push, id=_id)

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Редактирование пуш уведомления'
        return ctx


class PushDeleteView(CustomLoginRequiredMixin, DeleteView):
    success_url = '/pushes/'

    def get_object(self, queryset=None):
        _id = self.kwargs.get('pk')
        return get_object_or_404(Push, id=_id)

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Удаление пуш уведомления'
        return ctx


class OptionListView(CustomLoginRequiredMixin, ListView):
    model = Option
    context_object_name = 'options'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Список опций'
        return ctx

    def get_queryset(self):
        return Option.objects.filter(is_deleted=False)


class OptionDetailView(CustomLoginRequiredMixin, DetailView):
    model = Option

    def get_object(self, queryset=None):
        _id = self.kwargs.get('pk')
        return get_object_or_404(Option, id=_id)

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Просмотр опции'
        return ctx


class OptionCreateView(CustomLoginRequiredMixin, CreateView):
    form_class = OptionForm
    template_name = 'notifications/option_create.html'
    success_url = '/options/'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Создание опции'
        return ctx


class OptionUpdateView(CustomLoginRequiredMixin, UpdateView):
    form_class = OptionForm
    template_name = 'notifications/option_create.html'

    def get_object(self, queryset=None):
        _id = self.kwargs.get('pk')
        return get_object_or_404(Option, id=_id)

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Обновление опции'
        return ctx


class OptionDeleteView(CustomLoginRequiredMixin, DeleteView):
    success_url = '/options/'

    def get_object(self, queryset=None):
        _id = self.kwargs.get('pk')
        return get_object_or_404(Option, id=_id)

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Удаление опции'
        return ctx
