from django.shortcuts import render
from .models import Guineapig

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
  return render(request, 'guineapigs/detail.html', { 'guineapig': guineapig })