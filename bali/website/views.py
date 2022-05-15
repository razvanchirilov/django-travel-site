from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def gallery(request):
    return render(request, 'gallery.html', {})


def tours(request):
    return render(request, 'tours.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def contacts(request):
    return render(request, 'contacts.html', {})