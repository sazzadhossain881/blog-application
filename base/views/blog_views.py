from django.shortcuts import render


def index(request):
    diction = {}
    return render(request, "base/blog_list.html", context=diction)
