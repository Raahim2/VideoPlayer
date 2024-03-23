from django.contrib import admin

# Register your models here.
from .models import Patients , Doctors

admin.site.register(Patients)
admin.site.register(Doctors)

