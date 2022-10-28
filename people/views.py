from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from people.form import Form
from people.models import People


# Create your views here.
def index(request):
  people = People.objects.all()
  return render(request, 'people/index.html', {'people': people})


def details(request, id):
  onePeople = get_object_or_404(People, pk=id)
  return render(request, 'people/details.html', {'onePeople': onePeople})


def create(request):
  form = Form()
  if request.method == 'POST':
    form = Form(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/')
  else:
    form = Form()
    return render(request, 'people/form.html', {'form': form})


def update(request, id):
  obj = get_object_or_404(People, pk=id)

  form = Form(request.POST or None, instance = obj)

  if form.is_valid():
    form.save()
    return HttpResponseRedirect('/')

  return render(request, 'people/update.html', {'form': form})


def delete(request, id):
  onePeople = get_object_or_404(People, pk=id)
  if request.method == 'POST':
    onePeople.delete()
    return HttpResponseRedirect('/')
  return render(request, 'people/delete.html')
