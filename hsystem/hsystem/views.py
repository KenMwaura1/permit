from django.http import JsonResponse
from django.views import View
from permit import Permit
from .models import Patient
from django.conf import settings
from .serializers import PatientSerializer

class PatientDetailView(View):
    def get(self, request, patient_id):
        # Retrieve patient information from the database
        patient = Patient.objects.get(pk=patient_id)

        # Initialize the Permit client
        permit = Permit(
            api_key=settings.PERMIT_API_KEY,
            pdp_url=settings.PERMIT_PDP_URL
        )

        # Check ABAC policy for viewing patient records
        if not permit.is_allowed(
            subject=request.user,
            action='view',
            resource=patient
        ):
            return JsonResponse({'error': 'Permission denied'}, status=403)

        # Check ReBAC policy for viewing patient records
        if not permit.is_allowed(
            subject=request.user,
            action='view',
            resource=patient,
            relationships=[('treats', request.user, patient)]
        ):
            return JsonResponse({'error': 'Permission denied'}, status=403)

        # Serialize patient data
        serializer = PatientSerializer(patient)
        return JsonResponse(serializer.data)
    