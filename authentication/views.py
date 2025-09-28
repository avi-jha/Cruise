from http.client import HTTPResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import action
import re
from django.conf import settings

# Create your views here.


# onboarding views
class OnBoardingView(viewsets.ModelViewSet):

    @action(detail=False, methods=["POST"], url_path="onboard_user")
    def create_onboarding_request(self, request):
        payload = request.data.copy()
        errors = self.validate_payload(payload)
        if errors:
            return Response({"message": "Onboarding request could not be created.", "data": errors, "status": status.HTTP_400_BAD_REQUEST})
        
        return Response({"message": "Onboarding request created", "data": payload})

    def validate_payload(self, payload):
        
        error = {}
        
        # required fields
        required_fields = [
            "name",
            "surname",
            "phone",
            "dob",
            "email",
            "password",
            "gender"
        ]
        
        for field in required_fields:
            if not payload.get(field):
                error[field] = "This field is required."
            elif not str(payload.get(field).strip()):
                error[field] = "This field cannot be empty."
            elif field == "email": 
                if not re.fullmatch(settings.EMAIL_REGEX, payload.get(field)):
                    error[field] = f'Please enter a valid email.'
            elif field == "password":
                password = payload.get(field)
                
                if len(password) < 8:
                    error[field] = "Password length should be more than 8 characters."
                elif re.fullmatch(settings.PASSWORD_REGEX, password):
                    error[field] = "Password should be atlest 8 digit in length and contain 1 special character."
        return error
    
    
class SignUpView(viewsets.ModelViewSet):
    def get(self, request):
        return HTTPResponse("Sign Up Page")

    def post(self, request):
        return HTTPResponse("User signed up successfully")