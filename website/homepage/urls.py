from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("product1/", views.product1, name='product1'),
    path("product2/", views.product2, name='product2'),
    path("product3/", views.product3, name='product3'),
    path("product4/", views.product4, name='product4'),
]