from django.shortcuts import render, get_object_or_404

from .models import Blog, Vlog


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog.html',  {"blogs": blogs})


def vlog(request):
    vlogs = Vlog.objects.order_by("-data")
    return render(request, 'vlog/vlog.html', {"vlogs": vlogs})


def vlog_detail(request, vlog_id):
    vlog = get_object_or_404(Vlog, pk=vlog_id)
    return render(request, 'vlog/detail.html', {"vlog": vlog})


def about(request):
    return render(request, 'about/about.html')
