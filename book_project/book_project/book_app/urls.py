from django.urls import path
from .views import home_page,contact,profile,grades,add_user
urlpatterns = [
    path("home_page",home_page),
path("contact",contact),
path("profile",profile),
    path("grade/<int:marks>",grades),
    path("user/",add_user),
]
