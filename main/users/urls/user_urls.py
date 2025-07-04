from django.urls import path
from ..views.role_assign import (
    AssignExecutorView, AssignAssistantView, AssignAccountantView
)

urlpatterns = [
    path('<int:pk>/assign-executor/', AssignExecutorView.as_view()),
    path('<int:pk>/assign-assistant/', AssignAssistantView.as_view()),
    path('<int:pk>/assign-accountant/', AssignAccountantView.as_view()),
]