from django.shortcuts import render
from django.http import HttpResponse


class Guineapig: 
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

guineapigs = [
  Guineapig('Teddy', 'teddy', 'Likes lettuce.', 2),
  Guineapig('Snuggles', 'abyssinian', 'Loves to be brushed.', 1),
  Guineapig('Frodo', 'american', 'Fuzzy.', 4),
  Guineapig('Beelzebub', 'sheltie', 'Will bite you.', 3),
  Guineapig('Ross', 'skinny', 'Scared of noises.', 2),
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Herro!</h1>')

def about(request):
  return render(request, 'about.html')

def guineapigs_index(request):
  return render(request, 'guineapig/index.html', { 'guineapigs': guineapigs })