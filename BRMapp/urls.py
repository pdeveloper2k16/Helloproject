from django.conf.urls import url
from BRMapp import views


urlpatterns = [
    url('view-book', views.viewBook),
    url('new-book', views.newBook),
    url('edit-book', views.editBook),
    url('search-book', views.searchBook),
    url('delete-book', views.deleteBook),
    url(r'^add', views.add),
    url('edit', views.edit),
    url('search', views.search),
    url('login', views.userLogin),
    url('logout', views.userLogout),
]
