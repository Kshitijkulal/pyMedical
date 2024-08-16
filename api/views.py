from django.shortcuts import render

# Create your views here.
# views.py (add these to your existing views)

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_POST
from rest_framework.authtoken.models import Token
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Department, User, PatientRecord
from django.shortcuts import get_object_or_404

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(username, email, password, password2, is_doctor, is_patient, department):
    if not all([username, email, password, password2, is_doctor, is_patient, department]):
        raise ValueError("All fields are required")

    if password != password2:
        raise ValueError("Passwords do not match")

    try:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_doctor = is_doctor
        user.is_patient = is_patient
        user.department = department
        user.save()
        return user
    except Exception as e:
        # Handle specific exceptions like IntegrityError for unique constraint violations
        raise ValueError(f"Registration failed: {str(e)}")

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_user(request):
    user = authenticate(username=request.data.get('username'), password=request.data.get('password'))
    if user:
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def logout_user(request):
    logout(request)
    return Response(status=status.HTTP_200_OK)