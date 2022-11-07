from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Guineapig
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

class GuineapigCreate(CreateView):
  model = Guineapig
  fields = '__all__'

class GuineapigUpdate(UpdateView):
  model = Guineapig
  fields = ['breed', 'description', 'age']
  
class GuineapigDelete(DeleteView):
  model = Guineapig
  success_url = '/guineapigs/'