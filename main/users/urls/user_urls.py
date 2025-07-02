from django.urls import path
from ..views.role_assign import AssignExecutorView, AssignAssistantView

urlpatterns = [
    path('<int:pk>/assign-executor/', AssignExecutorView.as_view()),
    path('<int:pk>/assign-assistant/', AssignAssistantView.as_view()),
]