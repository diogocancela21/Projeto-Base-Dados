from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    
    path('zones/', views.ZoneListView.as_view(), name='zone-list'),
    path('zones/create/', views.ZoneCreateView.as_view(), name='zone-create'),
    path('zones/<int:pk>/', views.ZoneDetailView.as_view(), name='zone-detail'),
    path('zones/<int:pk>/edit/', views.ZoneUpdateView.as_view(), name='zone-update'),
    
    path('households/', views.HouseholdListView.as_view(), name='household-list'),
    path('households/create/', views.HouseholdCreateView.as_view(), name='household-create'),
    path('households/<int:pk>/', views.HouseholdDetailView.as_view(), name='household-detail'),
    path('households/<int:pk>/edit/', views.HouseholdUpdateView.as_view(), name='household-update'),
    
    path('residents/', views.ResidentListView.as_view(), name='resident-list'),
    path('residents/create/', views.ResidentCreateView.as_view(), name='resident-create'),
    path('residents/<int:pk>/', views.ResidentDetailView.as_view(), name='resident-detail'),
    path('residents/<int:pk>/edit/', views.ResidentUpdateView.as_view(), name='resident-update'),
    
    path('availabilities/', views.AvailabilityListView.as_view(), name='availability-list'),
    path('availabilities/create/', views.AvailabilityCreateView.as_view(), name='availability-create'),
    path('availabilities/<int:pk>/', views.AvailabilityDetailView.as_view(), name='availability-detail'),
    path('availabilities/<int:pk>/edit/', views.AvailabilityUpdateView.as_view(), name='availability-update'),
    
    path('mobility/', views.MobilityListView.as_view(), name='mobility-list'),
    path('mobility/create/', views.MobilityCreateView.as_view(), name='mobility-create'),
    path('mobility/<int:pk>/', views.MobilityDetailView.as_view(), name='mobility-detail'),
    path('mobility/<int:pk>/edit/', views.MobilityUpdateView.as_view(), name='mobility-update'),
    
    path('emergency/', views.EmergencyListView.as_view(), name='emergency-list'),
    path('emergency/create/', views.EmergencyCreateView.as_view(), name='emergency-create'),
    path('emergency/<int:pk>/', views.EmergencyDetailView.as_view(), name='emergency-detail'),
    path('emergency/<int:pk>/edit/', views.EmergencyUpdateView.as_view(), name='emergency-update'),

    path('incidents/', views.IncidentListView.as_view(), name='incident-list'),
    path('incidents/create/', views.IncidentCreateView.as_view(), name='incident-create'),
    path('incidents/<int:pk>/', views.IncidentDetailView.as_view(), name='incident-detail'),
    path('incidents/<int:pk>/edit/', views.IncidentUpdateView.as_view(), name='incident-update'),
]