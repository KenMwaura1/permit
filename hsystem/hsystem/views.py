from django.http import JsonResponse
from django.views import View
from permit.sync import Permit
from .models import Patient
from django.conf import settings
from .serializers import PatientSerializer
import json

class PatientDetailView(View):
    
    # Create a new patient record
    def post(self, request):
		# Deserialize patient data from request body
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
			# Save the patient to the database
            patient = serializer.save()
			# Initialize the Permit client
            permit = Permit(
				token=settings.PERMIT_API_KEY,
				pdp=settings.PERMIT_PDP_URL
			)
			# Check ABAC policy for creating patient records
            if not permit.check(
				subject=request.user,
				action='create',
				resource=patient
			):
                return JsonResponse({'error': 'Permission denied'}, status=403)
			# Check ReBAC policy for creating patient records
            if not permit.check(
				subject=request.user,
				action='create',
				resource=patient,
				relationships=[('treats', request.user, patient)]
			):
                return JsonResponse({'error': 'Permission denied'}, status=403)
			# Serialize patient data
            serializer = PatientSerializer(patient)
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
        
    # Retrieve patient information from the database    
    def get(self, request, patient_id):
        # Retrieve patient information from the database
        patient = Patient.objects.get(pk=patient_id)

        # Initialize the Permit client
        permit = Permit(
            token=settings.PERMIT_API_KEY,
            pdp=settings.PERMIT_PDP_URL
        )

        # Check ABAC policy for viewing patient records
        permitted = permit.check("Kenzmwaura1@gmail.com", "retrieve", "task") # default tenant is used
        if not permitted:
        	return JsonResponse({"result": f"John Smith is NOT PERMITTED to retrieve patient data!"}, status=403)
        
  
        # Check ReBAC policy for viewing patient records
        permitted = permit.check("Kenzmwaura1@gmail.com", "retrieve", "task") # default tenant is used
        if not permitted:
        	return JsonResponse({
			"result": f"John Smith is NOT PERMITTED to retrieve patient data!"
		}, status=403)

        # Serialize patient data
        serializer = PatientSerializer(patient)
        return JsonResponse(serializer.data)
    
	