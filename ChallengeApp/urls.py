from django.conf.urls import url
from ChallengeApp import views

urlpatterns = [
    url(r'^$', views.help, name='help'),
]
