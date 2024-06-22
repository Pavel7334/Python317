from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name="blog"),
    path('vlog/', views.vlog, name="vlog"),
    path('about/', views.about, name="about"),
    path('vlog/<int:vlog_id>/', views.vlog_detail, name="detail"),
]