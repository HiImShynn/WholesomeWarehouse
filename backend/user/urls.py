"""Docstring"""
from django.urls import path
from . import views

urlpatterns = [
    path('staff/', view=views.ListStaff.as_view(), name='list-staff'),
    path('create-staff/', view=views.CreateStaff.as_view(), name='create-staff'),
    path(
        'staff/<int:pk>/', 
        view=views.RetrieveUpdateDeleteStaff.as_view(),
        name='edit-staff',
    ),
    path('partner/', view=views.ListPartner.as_view(), name='list-partner'),
    path('create-partner/', view=views.CreatePartner.as_view(), name='create-partner'),
    path(
        'partner/<int:pk>/', 
        view=views.RetrieveUpdateDeletePartner.as_view(),
        name='edit-partner',
    ),
    path('register/', view=views.PartnerCreate.as_view(), name='partner-register'),
]
