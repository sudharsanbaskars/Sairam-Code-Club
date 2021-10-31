from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import ListView,DetailView
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator

from .forms import CreateUserForm, CreateEventForm, CreateGalleryForm
from .models import Event, Gallery

def home(request):
	events = Event.objects.all()
	images = Gallery.objects.all()
	context = {'events':events, 'images': images}
	return render(request, 'index.html', context=context)

class EventListView(ListView):
	model = Event
	paginate_by = 4
	template_name = "event_list.html"
	context_object_name = "events"

class EventDetailView(DetailView):
	model = Event
	template_name = "event_detail.html"
	context_object_name = "event"


