from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('blog/', views.blog, name='blog-detail'),
    path('portfolio/', views.portfolio, name='blog-portfolio'),
]
