from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import SessionForm  # You’ll create this next
from .models import Session


class Home(LoginView):
    template_name = 'home.html'


@login_required
def session_index(request):
    sessions = Session.objects.filter(coach=request.user)
    return render(request, 'index.html', {'sessions': sessions})


@login_required
def session_detail(request, session_id):
    session = get_object_or_404(Session, id=session_id)
    return render(request, 'detail.html', {'session': session})


class SessionCreate(LoginRequiredMixin, CreateView):
    model = Session
    fields = ['title', 'description', 'date', 'location']

    def form_valid(self, form):
        form.instance.coach = self.request.user
        return super().form_valid(form)


class SessionUpdate(LoginRequiredMixin, UpdateView):
    model = Session
    fields = ['title', 'description', 'date', 'location']


class SessionDelete(LoginRequiredMixin, DeleteView):
    model = Session
    success_url = '/sessions/'


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('session-index')
        else:
            error_message = 'Invalid sign up – try again'
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form, 'error_message': error_message})
