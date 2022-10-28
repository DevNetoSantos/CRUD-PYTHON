from django.forms import ModelForm
from people.models import People

class Form(ModelForm):
  class Meta:
    model = People
    fields = [
      'name',
      'email',
      'city'
    ]