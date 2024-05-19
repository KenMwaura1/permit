from rest_framework import serializers
from .models import Department, Patient, Doctor, Treatment


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'description']


class PatientSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    

    class Meta:
        model = Patient
        fields = '__all__'  


class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    department = DepartmentSerializer(read_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'user', 'department', 'specialty']


class TreatmentSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)
    patient = PatientSerializer(read_only=True)

    class Meta:
        model = Treatment
        fields = ['id', 'doctor', 'patient', 'start_date', 'end_date']
