from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'^register/', views.register),
    url(r'^upload',views.uploadPhoto),
    url(r'^logout/', views.logout),
    url(r'^login/', views.login),

]


