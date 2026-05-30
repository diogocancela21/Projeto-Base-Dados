from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Zone(models.Model):
    RISK_CHOICES = [
        (1, 'Baixo'),
        (2, 'Médio'),
        (3, 'Alto'),
    ]
    name = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    risk_level = models.IntegerField(choices=RISK_CHOICES, default=2)

    def __str__(self):
        return f"{self.name} ({self.municipality})"

    class Meta:
        verbose_name = "Zona de Intervenção"
        verbose_name_plural = "Zonas de Intervenção"


class Household(models.Model):
    PRIORITY_CHOICES = [
        (1, 'Muito Baixa'),
        (2, 'Baixa'),
        (3, 'Média'),
        (4, 'Alta'),
        (5, 'Muito Alta'),
    ]
    zone = models.ForeignKey(Zone, on_delete=models.PROTECT, related_name='households')
    address = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    evacuation_priority = models.IntegerField(
        default=1,
        choices=PRIORITY_CHOICES,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return f"{self.address[:40]}... [{self.zone}]"

    class Meta:
        verbose_name = "Agregado Familiar"
        verbose_name_plural = "Agregados Familiares"


class Resident(models.Model):
    household = models.ForeignKey(Household, on_delete=models.CASCADE, related_name='residents')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    phone = models.CharField(max_length=20)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Habitante"
        verbose_name_plural = "Habitantes"


class MobilityProfile(models.Model):
    resident = models.OneToOneField(Resident, on_delete=models.CASCADE, related_name='mobility')
    has_reduced_mobility = models.BooleanField(default=False)
    mobility_type = models.CharField(max_length=100, blank=True, default='')
    needs_assistance = models.BooleanField(default=False)
    notes = models.TextField(blank=True, default='')

    def __str__(self):
        return f"Perfil: {self.resident}"

    class Meta:
        verbose_name = "Perfil de Mobilidade"
        verbose_name_plural = "Perfis de Mobilidade"


class MonthlyAvailability(models.Model):
    STATUS_CHOICES = [
        ('home', 'Em casa'),
        ('abroad', 'No estrangeiro'),
        ('unavailable', 'Indisponível'),
    ]
    household = models.ForeignKey(Household, on_delete=models.CASCADE, related_name='availabilities')
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.household} - {self.month}/{self.year}: {self.get_status_display()}"

    class Meta:
        verbose_name = "Disponibilidade Mensal"
        verbose_name_plural = "Disponibilidades Mensais"


class EmergencyContact(models.Model):
    household = models.ForeignKey(Household, on_delete=models.CASCADE, related_name='emergency_contacts')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    relationship = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.relationship})"

    class Meta:
        verbose_name = "Contacto de Emergência"
        verbose_name_plural = "Contactos de Emergência"


class Incident(models.Model):
    TYPE_CHOICES = [
        ('fire', 'Incêndio'),
        ('flood', 'Cheia'),
        ('landslide', 'Tempestade'),
        ('other', 'Outro'),
    ]
    zone = models.ForeignKey(Zone, on_delete=models.PROTECT, related_name='incidents')
    incident_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    date_reported = models.DateField(auto_now_add=True)
    severity = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    status = models.CharField(max_length=20, choices=[('active', 'Ativo'), ('controlled', 'Controlado'), ('resolved', 'Resolvido')], default='active')
    notes = models.TextField(blank=True, default='')

    def __str__(self):
        return f"{self.get_incident_type_display()} - {self.zone} ({self.date_reported})"

    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"