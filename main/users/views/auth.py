from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions
from ..serializers.auth import RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


@extend_schema(
    tags=["Authentication"],
    summary="Регистрация нового пользователя",
    request=RegisterSerializer,
    responses={201: RegisterSerializer, 400: dict},
)
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]