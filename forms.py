from django import forms
from .models import Household, Resident, MonthlyAvailability, Zone, MobilityProfile, EmergencyContact, Incident

class ZoneForm(forms.ModelForm):
    class Meta:
        model = Zone
        fields = ['name', 'municipality', 'risk_level']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'municipality': forms.TextInput(attrs={'class': 'form-control'}),
            'risk_level': forms.Select(attrs={'class': 'form-select'}),
        }

class HouseholdForm(forms.ModelForm):
    class Meta:
        model = Household
        fields = ['zone', 'address', 'latitude', 'longitude', 'evacuation_priority']
        widgets = {
            'zone': forms.Select(attrs={'class': 'form-select'}),
            'address': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'evacuation_priority': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = ['household', 'first_name', 'last_name', 'birth_date', 'phone', 'is_primary']
        widgets = {
            'household': forms.Select(attrs={'class': 'form-select'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'is_primary': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class MonthlyAvailabilityForm(forms.ModelForm):
    class Meta:
        model = MonthlyAvailability
        fields = ['household', 'year', 'month', 'status', 'return_date']
        widgets = {
            'household': forms.Select(attrs={'class': 'form-select'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'month': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'return_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class MobilityProfileForm(forms.ModelForm):
    class Meta:
        model = MobilityProfile
        fields = ['resident', 'has_reduced_mobility', 'mobility_type', 'needs_assistance', 'notes']
        widgets = {
            'resident': forms.Select(attrs={'class': 'form-select'}),
            'has_reduced_mobility': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'mobility_type': forms.TextInput(attrs={'class': 'form-control'}),
            'needs_assistance': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }

class EmergencyContactForm(forms.ModelForm):
    class Meta:
        model = EmergencyContact
        fields = ['household', 'name', 'phone', 'relationship']
        widgets = {
            'household': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'relationship': forms.TextInput(attrs={'class': 'form-control'}),
        }

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['zone', 'incident_type', 'severity', 'status', 'notes']
        widgets = {
            'zone': forms.Select(attrs={'class': 'form-select'}),
            'incident_type': forms.Select(attrs={'class': 'form-select'}),
            'severity': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
