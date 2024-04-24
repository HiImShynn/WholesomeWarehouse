"""DOCSTRING"""
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
# from . import views

class MyTokenVerifyView(TokenVerifyView):
    def finalize_response(self, request, response, *args, **kwargs):
        print(request.user)
        return super().finalize_response(request, response, *args, **kwargs)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/verify', MyTokenVerifyView.as_view(), name='token-verify'),
]
