from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions
from ..serializers.profile import UserMeSerializer


@extend_schema(
    tags=["Profile"],
    summary="Получить информацию о текущем пользователе",
    responses=UserMeSerializer,
)
class MeView(generics.RetrieveAPIView):
    serializer_class = UserMeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user