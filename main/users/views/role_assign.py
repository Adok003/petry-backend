from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from ..models import CustomUser
from ..serializers.role_assign import UserSimpleSerializer
from ..permissions import IsSuperAdmin, IsExecutor
from ..services.role_manager import assign_executor, assign_assistant, assign_accountant

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
            return Response({"detail": "Нельзя изменить собственную роль."}, status=403)
        assign_executor(user, assigned_by=request.user)  # <-- передаём кто назначил
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

@extend_schema(
    tags=["Role Management"],
    summary="Назначить пользователя бухгалтером (только для ЧСИ)",
    responses={200: dict, 400: dict, 403: dict},
)
class AssignAccountantView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSimpleSerializer
    permission_classes = [permissions.IsAuthenticated, IsExecutor]

    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        if user == request.user:
            return Response({"detail": "Нельзя изменить собственную роль."}, status=403)
        assign_accountant(user, request.user)
        return Response({"detail": f"{user.email} назначен как бухгалтер"})

