from django.urls import path
from branches_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("branches/", views.branches_list, name="branches-list"),
    path("branches/<int:pk>/", views.branch_update, name="branches-update"),
]
