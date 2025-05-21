from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
# ✅ Clients: view available sessions
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import SessionForm
from .models import Application, Profile, Session  # ✅ Profile imported


class Home(LoginView):
    template_name = 'home.html'




class AvailableSessions(ListView):  # Removed LoginRequiredMixin
    model = Session
    template_name = 'coaching/available_sessions.html'
    context_object_name = 'sessions'


# ✅ Session detail & reservation
class SessionDetail(LoginRequiredMixin, DetailView):
    model = Session
    template_name = 'coaching/session_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        session = self.get_object()
        context['has_applied'] = session.application_set.filter(applicant=self.request.user).exists()
        return context

    def post(self, request, *args, **kwargs):
        session = self.get_object()
        if session.coach == request.user:
            return redirect('session-detail', pk=session.pk)

        if not session.application_set.filter(applicant=request.user).exists():
            Application.objects.create(session=session, applicant=request.user)

        return redirect('session-detail', pk=session.pk)


# ✅ Coach: view their sessions
@login_required
def session_index(request):
    sessions = Session.objects.filter(coach=request.user)
    return render(request, 'coaching/index.html', {'sessions': sessions})


# ✅ Coach: create session
class SessionCreate(LoginRequiredMixin, CreateView):
    model = Session
    form_class = SessionForm

    def form_valid(self, form):
        form.instance.coach = self.request.user
        return super().form_valid(form)


# ✅ Coach: update session
class SessionUpdate(LoginRequiredMixin, UpdateView):
    model = Session
    form_class = SessionForm


# ✅ Coach: delete session
class SessionDelete(LoginRequiredMixin, DeleteView):
    model = Session
    success_url = '/sessions/'


# ✅ Signup (with role)
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        role = request.POST.get('role')
        if form.is_valid() and role in ['coach', 'client']:
            user = form.save()
            Profile.objects.create(user=user, role=role)  # ✅ save role manually
            login(request, user)
            return redirect('session-index')
        else:
            error_message = 'Invalid sign up – try again or select a role.'
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {
        'form': form,
        'error_message': error_message
    })


# ✅ Client: view reservations
class ApplicationListView(LoginRequiredMixin, ListView):
    model = Application
    template_name = 'coaching/applications_list.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user)


# ✅ Client: cancel reservation
class ApplicationDeleteView(LoginRequiredMixin, DeleteView):
    model = Application
    template_name = 'coaching/application_confirm_delete.html'
    success_url = reverse_lazy('my-reservations')

    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user)
