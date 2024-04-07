"""DOCSTRING"""
import json
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.http import require_POST
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

def get_csrf(request):
    """DOCSTRING"""
    response = JsonResponse(
        {
            'detail': 'CSRF Cookie set.'
        }
    )
    response['X-CSRFToken'] = get_token(request=request)
    return response

@require_POST
def login_view(request):
    """DOCSTRING"""
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    if username is None or password is None:
        return JsonResponse(
            {
                'detail': 'Please provide username and password.',
            }, status = 400,
        )

    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse(
            {
                'detail': 'Invalid credentials.'
            }, status = 400,
        )

    login(request, user)
    return JsonResponse(
        {
            'detail': 'Successfully logged in.'
        }, status = 200,
    )

def logout_view(request):
    """DOCSTRING"""
    if not request.user.is_authenticated:
        return JsonResponse(
            {
                'detail': 'You are not logged in.'
            }, status = 400,
        )

    logout(request)
    return JsonResponse(
        {
            'detail': 'Successfully logged out.'
        }, status = 200,
    )

class SessionView(APIView):
    """DOSCTRING"""
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, format = None):
        """DOCSTRING"""
        return JsonResponse(
            {
                'isAuthenticated': True,
            }, status = 200,
        )

class WhoAmIView(APIView):
    """DOCSTRING"""
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, format = None):
        """DOCSTRING"""
        return JsonResponse(
            {
                'username': request.user.username
            }, status = 200,
        )
