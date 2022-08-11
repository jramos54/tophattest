from django.urls import path
from . import views

urlpatterns=[
  path('',views.home,name='home'),
  path('addForum/',views.addForum,name='addForum'),
  path('addDiscussion',views.addDiscussion,name='addDiscussion')
]