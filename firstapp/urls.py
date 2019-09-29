from django.conf.urls import url
from firstapp import views


urlpatterns = [
    url('^$', views.greeting),
    url('about/',views.about),
    url('contact/', views.showContact),

]