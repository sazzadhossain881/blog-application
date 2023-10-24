from django.urls import path
from base.views import blog_views as views

app_name = "blog"

urlpatterns = [
    path("list/", views.index, name="blog-list"),
]
