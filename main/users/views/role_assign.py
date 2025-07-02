from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from ..models import CustomUser
from ..serializers.role_assign import UserSimpleSerializer
from ..permissions import IsSuperAdmin, IsExecutor
from ..services.role_manager import assign_executor, assign_assistant

@extend_schema(
    tags=["Role Management"],
    summary="Назначить пользователя как ЧСИ (только для Суперадмина)",
    responses={200: dict, 400: dict, 403: dict},
)
class AssignExecutorView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSimpleSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def patch(self, request, *args, **kwargs):
        user = self.get_object()

        if user == request.user:
            return Response({"detail": "Нельзя изменить свою собственную роль."}, status=400)

        assign_executor(user)
        return Response({"detail": f"{user.email} назначен как ЧСИ"})

@extend_schema(
    tags=["Role Management"],
    summary="Назначить пользователя помощником (только для ЧСИ)",
    responses={200: dict, 400: dict, 403: dict},
)
class AssignAssistantView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSimpleSerializer
    permission_classes = [permissions.IsAuthenticated, IsExecutor]

    def patch(self, request, *args, **kwargs):
        user = self.get_object()

        if user == request.user:
            return Response({"detail": "Нельзя назначить себя помощником."}, status=400)

        assign_assistant(user, request.user)
        return Response({"detail": f"{user.email} назначен как помощник"})

