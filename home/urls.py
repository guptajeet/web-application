from django.contrib import admin
from django.urls import path, include

from home import views

# django admin header customization
admin.site.site_header = "Login to Ajeet Gupta"
admin.site.site_title = "Welcome to Ajeet's Dashboard"
admin.site.index_title = "Welcome to this portal"
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
    path('search/', views.search, name="search"),
    path('wdp1/',views.wdp1,name="wdp1"),
    path('', views.mbook,name="mbook"),
    path('mbook', views.mbook,name="mbook"),
    path('show',views.show,name="show"),
    path('edit/<str:bname>', views.edit,name="edit"),
    path('update/<str:bname>', views.update,name="update"),
    path('delete/<str:bname>', views.destroy,name="delete"),
]

