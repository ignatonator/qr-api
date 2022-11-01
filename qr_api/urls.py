from django.urls import path

# Import the home view
from . import views

app_name = "url_short"

urlpatterns = [
    # Home view
    path("", views.home_view, name="home"),

]