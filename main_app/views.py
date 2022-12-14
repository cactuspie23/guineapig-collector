from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Guineapig, Accessory
from .forms import FeedingForm

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def guineapigs_index(request):
  guineapigs = Guineapig.objects.filter(user=request.user)
  return render(request, 'guineapigs/index.html', { 'guineapigs': guineapigs })

@login_required
def guineapigs_detail(request, guineapig_id):
  guineapig = Guineapig.objects.get(id=guineapig_id)
  accessories_guineapig_doesnt_have = Accessory.objects.exclude(id__in = guineapig.accessories.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'guineapigs/detail.html', { 'guineapig': guineapig, 'feeding_form': feeding_form, 'accessories': accessories_guineapig_doesnt_have })

@login_required
def add_feeding(request, guineapig_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.guineapig_id = guineapig_id
    new_feeding.save()
  return redirect('guineapigs_detail', guineapig_id=guineapig_id)

@login_required
def assoc_accessory(request, guineapig_id, accessory_id):
  Guineapig.objects.get(id=guineapig_id).accessories.add(accessory_id)
  return redirect('guineapigs_detail', guineapig_id=guineapig_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('guineapigs_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

class GuineapigCreate(LoginRequiredMixin, CreateView):
  model = Guineapig
  fields = ['name', 'breed', 'description', 'age']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class GuineapigUpdate(LoginRequiredMixin, UpdateView):
  model = Guineapig
  fields = ['breed', 'description', 'age']
  
class GuineapigDelete(LoginRequiredMixin, DeleteView):
  model = Guineapig
  success_url = '/guineapigs/'

class AccessoryCreate(LoginRequiredMixin, CreateView):
  model = Accessory
  fields = '__all__'

class AccessoryList(LoginRequiredMixin, ListView):
  model = Accessory

class AccessoryDetail(LoginRequiredMixin, DetailView):
  model = Accessory

class AccessoryUpdate(LoginRequiredMixin, UpdateView):
  model = Accessory
  fields = ['name', 'color']

class AccessoryDelete(LoginRequiredMixin, DeleteView):
  model = Accessory
  success_url = '/accessories/'