from django.contrib import admin
from .models import Zone, Household, Resident, MobilityProfile, MonthlyAvailability, EmergencyContact, Incident

@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'municipality', 'risk_level')
    search_fields = ('name', 'municipality')
    list_filter = ('risk_level',)
    ordering = ('municipality', 'name')

@admin.register(Household)
class HouseholdAdmin(admin.ModelAdmin):
    list_display = ('address', 'zone', 'evacuation_priority')
    search_fields = ('address',)
    list_filter = ('zone', 'evacuation_priority')
    ordering = ('zone', 'address')

@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'household', 'phone', 'is_primary')
    search_fields = ('first_name', 'last_name', 'phone')
    list_filter = ('household', 'is_primary')
    ordering = ('household', 'last_name')

@admin.register(MobilityProfile)
class MobilityProfileAdmin(admin.ModelAdmin):
    list_display = ('resident', 'has_reduced_mobility', 'needs_assistance')
    list_filter = ('has_reduced_mobility', 'needs_assistance')
    search_fields = ('resident__first_name', 'resident__last_name')

@admin.register(MonthlyAvailability)
class MonthlyAvailabilityAdmin(admin.ModelAdmin):
    list_display = ('household', 'year', 'month', 'status', 'return_date')
    list_filter = ('status', 'year', 'month')
    search_fields = ('household__address',)
    ordering = ('-year', '-month')

@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'household', 'phone', 'relationship')
    search_fields = ('name', 'phone', 'relationship')
    list_filter = ('household', 'relationship')

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('date_reported', 'zone', 'get_incident_type_display', 'severity', 'status')
    list_filter = ('incident_type', 'status', 'zone')
    search_fields = ('zone__name', 'notes')