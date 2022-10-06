from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Character, Quote, Quotelist
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
class QuoteLists(TemplateView):
    template_name = "quote_lists.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quotelists'] = Quotelist.objects.all()
        return context

class QuotelistQuoteAssoc(View):

    def get(self, request, pk, quote_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the playlist by the id and
            # remove from the join table the given song_id
            Quotelist.objects.get(pk=pk).quotes.remove(quote_pk)
        if assoc == "add":
            # get the playlist by the id and
            # add to the join table the given song_id
            Quotelist.objects.get(pk=pk).quotes.add(quote_pk)
        return redirect('/quote-lists/')

class CharacterDetail(DetailView):
    model = Character
    template_name = "character_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["quotelists"] = Quotelist.objects.all()
        return context

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)


