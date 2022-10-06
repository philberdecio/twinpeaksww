from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Character, Quote, Quotelist
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse

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

class CharacterUpdate(UpdateView):
    model = Character
    fields = ['name', 'img', 'aka', 'bio', 'see_also']
    template_name = "character_update.html"
    
    def get_success_url(self):
        return reverse('character_detail', kwargs={'pk': self.object.pk})

class CharacterDelete(DeleteView):
    model = Character
    template_name = "character_delete_confirmation.html"
    success_url = "/characters/"

class QuoteCreate(View):

    def post(self, request, pk):
        quote = request.POST.get("quote")
        character = Character.objects.get(pk=pk)
        Quote.objects.create(quote=quote, character=character)
        return redirect('character_detail', pk=pk)

class QuoteLists(TemplateView):
    template_name = "quote_lists.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quotelists'] = Quotelist.objects.all()
        return context
