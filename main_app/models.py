from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

MEALS = (
  ('H', 'Hay'),
  ('P', 'Pellets'),
  ('L', 'Lettuce'),
  ('B', 'Bell Pepper'),
  ('A', 'Apples'),
  ('O', 'Oranges'),
)

class Accessory(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('accessories_detail', kwargs={'pk': self.id})

class Guineapig(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  accessories = models.ManyToManyField(Accessory)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('guineapigs_detail', kwargs={'guineapig_id': self.id})

  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
  date = models.DateField('Feeding Date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )

  guineapig = models.ForeignKey(Guineapig, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"

  class Meta:
    ordering = ['-date']
