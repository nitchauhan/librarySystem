from django.contrib import admin
from django.urls import path, include
from . import views

admin.site.site_header = "library system Admin"
admin.site.site_title = "library system Admin Portal"
admin.site.index_title = "Welcome to library system Portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('addbook', views.addbook, name='addbook'),
    path('viewbook', views.viewbook, name='viewbook'),
    path('issuebook', views.issuebook, name='issuebook'),
    # path('purchasebook', views.purchasebook, name='purchasebook'),
    path('purchaseviewbook', views.purchaseviewbook, name='purchaseviewbook'),
    path('viewissuebook', views.viewissuebook, name='viewissuebook'),
    path('contact', views.contact, name='contact'),
    path('signup', views.signupHandle, name='signupHandle'),
    path('login', views.loginHandle, name='loginHandle'),
    path('logout', views.logoutHandle, name='logoutHandle'),
    path('search', views.search, name='query'),
    path('edit/<int:bookid>', views.edit, name='edit'),
    path('purchasebook/<int:bookid>', views.purchasebook, name='purchasebook'),
    path('delete/<int:bookid>', views.delete, name='delete')
    
]
