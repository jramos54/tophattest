from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import forum, discussion
from .forms import CreateDiscussion,CreateForum

# Create your views here.
def home(request):
  template=loader.get_template('home.html')
  forums=forum.objects.all()
  count=forums.count()
  discussions=[]
  for i in forums:
    discussions.append(i.discussion_set.all())

  context={
    'forums':forums,
    'count':count,
    'discussions':discussions
  }

  return HttpResponse(template.render(context,request))
  
  
def addForum(request):
  template=loader.get_template('addForum.html')
  form=CreateForum()
  if request.method == 'POST':
    form=CreateForum(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/')
  context={
    'form':form
  }

  return HttpResponse(template.render(context,request))

def addDiscussion(request):
  template=loader.get_template('addDiscussion.html')
  form=CreateDiscussion()
  if request.method =='POST':
    form = CreateDiscussion(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/')
  context={
    'form':form
  }
  return HttpResponse(template.render(context,request))