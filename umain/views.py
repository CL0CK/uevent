from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView, CreateView

# from uevent.umain.forms import AddEventForm

from .models import *
from .forms import *


# Create your views here.
menu = [
    {'title': "About site", 'url_name': 'about'},
    {'title': "Add new event", 'url_name': 'add_event'},
    {'title': "Contact us", 'url_name': 'contact'},
    {'title': "Sign in", 'url_name': 'login'}
]


class EventHome(ListView):
    model = Event
    template_name = 'umain/index.html'
    context_object_name = 'events'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Main page'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Event.objects.filter(is_published=True)


# def index(request):
#     # Пример вызова шаблона
#     events = Event.objects.all()
#     cats = Category.objects.all()

#     context = {
#         'events': events,
#         'cats': cats,
#         'menu': menu,
#         'title': 'Main page',
#         'cat_selected': 0,
#     }

#     return render(request, 'umain/index.html', context=context)


def about(request):
    # Пример вызова шаблона
    return render(request, 'umain/about.html', {'menu': menu, 'title': 'About site'})


class AddEvent(CreateView):
    form_class = AddEventForm
    template_name = 'umain/addevent.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Add event'
        return context

# def addevent(request):
#     if request.method == 'POST':
#         form = AddEventForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')

#     else:
#         form = AddEventForm()
#     return render(request, 'umain/addevent.html', {'form': form, 'menu': menu, 'title': 'Add event'})


def contact(request):
    return HttpResponse("Conctact us")


def login(request):
    return HttpResponse("Sign in")


# def show_event(request, event_slug):
#     event = get_object_or_404(Event, slug=event_slug)

#     context = {
#         'event': event,
#         'menu': menu,
#         'title': event.title,
#         'cat_selected': event.cat_id,
#     }
#     return render(request, 'umain/event.html', context=context)

class ShowEvent(DetailView):
    model = Event
    template_name = 'umain/event.html'
    slug_url_kwarg = 'event_slug'
    context_object_name = 'event'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['event']
        return context


class EventCategory(ListView):
    model = Event
    template_name = 'umain/index.html'
    context_object_name = 'events'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Category - '+str(context['events'][0].cat)
        context['cat_selected'] = context['events'][0].cat_id
        return context

    def get_queryset(self):
        return Event.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


# def show_category(request, cat_slug):
#     events = Event.objects.filter(cat__slug=cat_slug)
#     cats = Category.objects.all()

#     if len(events) == 0:
#         raise Http404()

#     context = {
#         'events': events,
#         'cats': cats,
#         'menu': menu,
#         'title': 'Main page',
#         'cat_selected': cat_slug,
#     }
#     return render(request, 'umain/index.html', context=context)


# def categories(request, catid):
#     if(request.GET):
#         print(request.GET)
#     return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


# def archive(request, year):
#     if int(year) > 2020:
#         return redirect('main', permanent=True)  # Вернёт на главную страницу
#     return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")
