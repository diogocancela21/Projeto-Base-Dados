from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Zone, Household, Resident, MonthlyAvailability, MobilityProfile, EmergencyContact, Incident
from .forms import (
    ZoneForm, HouseholdForm, ResidentForm, 
    MonthlyAvailabilityForm, MobilityProfileForm, EmergencyContactForm, IncidentForm
)

class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'counts'

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['counts'] = {
            'zones': Zone.objects.count(),
            'households': Household.objects.count(),
            'residents': Resident.objects.count(),
            'availabilities': MonthlyAvailability.objects.count(),
            'mobility': MobilityProfile.objects.count(),
            'contacts': EmergencyContact.objects.count(),
            'incidents': Incident.objects.count(),
        }
        return context

# Zone Views
class ZoneListView(ListView):
    model = Zone
    template_name = 'zone_list.html'
    context_object_name = 'zones'
class ZoneDetailView(DetailView):
    model = Zone
    template_name = 'zone_detail.html'
    context_object_name = 'zone'
class ZoneCreateView(CreateView):
    model = Zone
    form_class = ZoneForm
    template_name = 'zone_form.html'
    success_url = reverse_lazy('zone-list')
class ZoneUpdateView(UpdateView):
    model = Zone
    form_class = ZoneForm
    template_name = 'zone_form.html'
    success_url = reverse_lazy('zone-list')

# Household Views
class HouseholdListView(ListView):
    model = Household
    template_name = 'household_list.html'
    context_object_name = 'households'
class HouseholdDetailView(DetailView):
    model = Household
    template_name = 'household_detail.html'
    context_object_name = 'household'
class HouseholdCreateView(CreateView):
    model = Household
    form_class = HouseholdForm
    template_name = 'household_form.html'
    success_url = reverse_lazy('household-list')
class HouseholdUpdateView(UpdateView):
    model = Household
    form_class = HouseholdForm
    template_name = 'household_form.html'
    success_url = reverse_lazy('household-list')

# Resident Views
class ResidentListView(ListView):
    model = Resident
    template_name = 'resident_list.html'
    context_object_name = 'residents'
class ResidentDetailView(DetailView):
    model = Resident
    template_name = 'resident_detail.html'
    context_object_name = 'resident'
class ResidentCreateView(CreateView):
    model = Resident
    form_class = ResidentForm
    template_name = 'resident_form.html'
    success_url = reverse_lazy('resident-list')
class ResidentUpdateView(UpdateView):
    model = Resident
    form_class = ResidentForm
    template_name = 'resident_form.html'
    success_url = reverse_lazy('resident-list')

# MonthlyAvailability Views
class AvailabilityListView(ListView):
    model = MonthlyAvailability
    template_name = 'monthlyavailability_list.html'
    context_object_name = 'availabilities'
class AvailabilityDetailView(DetailView):
    model = MonthlyAvailability
    template_name = 'monthlyavailability_detail.html'
    context_object_name = 'availability'
class AvailabilityCreateView(CreateView):
    model = MonthlyAvailability
    form_class = MonthlyAvailabilityForm
    template_name = 'monthlyavailability_form.html'
    success_url = reverse_lazy('availability-list')
class AvailabilityUpdateView(UpdateView):
    model = MonthlyAvailability
    form_class = MonthlyAvailabilityForm
    template_name = 'monthlyavailability_form.html'
    success_url = reverse_lazy('availability-list')

# MobilityProfile Views
class MobilityListView(ListView):
    model = MobilityProfile
    template_name = 'mobility_list.html'
    context_object_name = 'profiles'
class MobilityDetailView(DetailView):
    model = MobilityProfile
    template_name = 'mobility_detail.html'
    context_object_name = 'profile'
class MobilityCreateView(CreateView):
    model = MobilityProfile
    form_class = MobilityProfileForm
    template_name = 'mobility_form.html'
    success_url = reverse_lazy('mobility-list')
class MobilityUpdateView(UpdateView):
    model = MobilityProfile
    form_class = MobilityProfileForm
    template_name = 'mobility_form.html'
    success_url = reverse_lazy('mobility-list')

# EmergencyContact Views
class EmergencyListView(ListView):
    model = EmergencyContact
    template_name = 'emergencycontact_list.html'
    context_object_name = 'contacts'
class EmergencyDetailView(DetailView):
    model = EmergencyContact
    template_name = 'emergencycontact_detail.html'
    context_object_name = 'contact'
class EmergencyCreateView(CreateView):
    model = EmergencyContact
    form_class = EmergencyContactForm
    template_name = 'emergencycontact_form.html'
    success_url = reverse_lazy('emergency-list')
class EmergencyUpdateView(UpdateView):
    model = EmergencyContact
    form_class = EmergencyContactForm
    template_name = 'emergencycontact_form.html'
    success_url = reverse_lazy('emergency-list')
class IncidentListView(ListView):
    model = Incident
    template_name = 'incident_list.html'
    context_object_name = 'incidents'
class IncidentDetailView(DetailView):
    model = Incident
    template_name = 'incident_detail.html'
    context_object_name = 'incident'
class IncidentCreateView(CreateView):
    model = Incident
    form_class = IncidentForm
    template_name = 'incident_form.html'
    success_url = reverse_lazy('incident-list')
class IncidentUpdateView(UpdateView):
    model = Incident
    form_class = IncidentForm
    template_name = 'incident_form.html'
    success_url = reverse_lazy('incident-list')