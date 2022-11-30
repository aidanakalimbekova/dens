from core.models import Doctor, Patient
from django.contrib import admin

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)


class PatientAdmin(admin.ModelAdmin):
    list = ('birth_date', 'iin', 'patient_id', 'name', 'surname', 'middle_name', 'blood_group', 'emergency_contact_number', 'contact_number', 'email', 'address', 'marital_status', 'registration_date')

    admin.site.register(Patient)

class DoctorAdmin(admin.ModelAdmin):
    list = ('birth_date', 'iin', 'doctor_id', 'name', 'surname', 'middle_name', 'department_id', 'specialization_id', 'experience', 'photo', 'category', 'price', 'schedule_details', 'education', 'rating', 'address')

    admin.site.register(Patient)