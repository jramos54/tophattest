from django.forms import ModelForm
from .models import forum,discussion

class CreateForum(ModelForm):
  class Meta:
    model=forum
    fields="__all__"

class CreateDiscussion(ModelForm):
  class Meta:
    model=discussion
    fields="__all__"