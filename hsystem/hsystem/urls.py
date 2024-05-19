"""
URL configuration for hsystem project.

"""
from django.contrib import admin
from django.urls import path
from .views import PatientDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
	 path('patients/<int:patient_id>/', PatientDetailView.as_view(), name='patient-detail'),
]
