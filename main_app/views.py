from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Guineapig, Accessory
from .forms import FeedingForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def guineapigs_index(request):
  guineapigs = Guineapig.objects.all()
  return render(request, 'guineapigs/index.html', { 'guineapigs': guineapigs })

def guineapigs_detail(request, guineapig_id):
  guineapig = Guineapig.objects.get(id=guineapig_id)
  feeding_form = FeedingForm()
  return render(request, 'guineapigs/detail.html', { 'guineapig': guineapig, 'feeding_form': feeding_form })

def add_feeding(request, guineapig_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.guineapig_id = guineapig_id
    new_feeding.save()
  return redirect('guineapigs_detail', guineapig_id=guineapig_id)

class GuineapigCreate(CreateView):
  model = Guineapig
  fields = '__all__'

class GuineapigUpdate(UpdateView):
  model = Guineapig
  fields = ['breed', 'description', 'age']
  
class GuineapigDelete(DeleteView):
  model = Guineapig
  success_url = '/guineapigs/'

class AccessoryCreate(CreateView):
  model = Accessory
  fields = '__all__'

class AccessoryList(ListView):
  model = Accessory

class AccessoryDetail(DetailView):
  model = Accessory

class AccessoryUpdate(UpdateView):
  model = Accessory
  fields = ['name', 'color']

class AccessoryDelete(DeleteView):
  model = Accessory
  success_url = '/accessories/'