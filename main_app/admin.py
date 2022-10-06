from django.contrib import admin
from .models import Character, Quote, Quotelist

# Register your models here.
admin.site.register(Character)
admin.site.register(Quote)
admin.site.register(Quotelist)
