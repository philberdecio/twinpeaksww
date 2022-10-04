from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Character
from django.views.generic.edit import CreateView
from django.views.generic import DetailView

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class CharacterList(TemplateView):
    template_name = "character_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["characters"] = Character.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["characters"] = Character.objects.all()
        return context

class CharacterCreate(CreateView):
    model = Character
    fields = ['name', 'img', 'aka', 'bio', 'see_also']
    template_name = "character_create.html"
    success_url = "/characters/"

class CharacterDetail(DetailView):
    model = Character
    template_name = "character_detail.html"
