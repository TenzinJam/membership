from django.conf.urls import url
from MembershipApp import views

urlpatterns = [
  url(r'^members$', views.MembershipApi),
  url(r'^members/validate$', views.MembershipApi)
]
