from django.shortcuts import render
from django.http import HttpResponse


class Guineapig: 
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

guineapigs = [
  Guineapig('Teddy', 'teddy', 'Likes a good bell pepper.', 2),
  Guineapig('Snuggles', 'abyssinian', 'Loves to be brushed.', 1),
  Guineapig('Frodo', 'american', 'Squeaks when you open the fridge.', 4),
  Guineapig('Beelzebub', 'sheltie', 'Will bite you.', 3),
  Guineapig('Ross', 'peruvian', 'Scared of all noises.', 2),
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Herro!</h1>')

def about(request):
  return render(request, 'about.html')

def guineapigs_index(request):
  return render(request, 'guineapigs/index.html', { 'guineapigs': guineapigs })