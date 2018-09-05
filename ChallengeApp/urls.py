from django.conf.urls import url
from ChallengeApp import views

urlpatterns = [
    url(r'^$', views.users, name='users'),
]
