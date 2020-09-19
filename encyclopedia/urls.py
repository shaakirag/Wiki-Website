from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("<str:title>/edit/", views.edit, name="edit"),
    path("new/", views.new, name="new"),
    path("<str:title>/delete/", views.delete, name="delete"),
    path("random/", views.random_function, name="random")
]
