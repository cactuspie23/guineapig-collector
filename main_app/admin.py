from django.contrib import admin
from .models import Guineapig, Feeding, Accessory

# Register your models here.
admin.site.register(Guineapig)
admin.site.register(Feeding)
admin.site.register(Accessory)