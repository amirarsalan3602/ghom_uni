from django.urls import path
from home import views

app_name = "home"

urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    path("submit_comment/", views.CommentsView.as_view(), name="submit_comment")
]
