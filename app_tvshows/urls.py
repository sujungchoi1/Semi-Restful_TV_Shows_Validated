from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.newShows),
    path('processNewShows', views.processNewShows),
    path('shows/<int:show_id>', views.showDetail),
    path('shows/<int:show_id>/edit', views.edit),
    path('<int:show_id>/processEdit', views.processEdit),
    path('<int:show_id>/delete', views.delete)
]
