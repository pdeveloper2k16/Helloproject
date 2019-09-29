from django.conf.urls import url
from secondapp import views

urlpatterns = [
    url('employee/', views.employee_info_views),
    url('test/', views.showTest),
    url('result/', views.result),

]
