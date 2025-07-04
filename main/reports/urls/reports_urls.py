from django.urls import path
from ..views.report4 import Report4UploadView

urlpatterns = [
    path('report4/upload/', Report4UploadView.as_view()),
]