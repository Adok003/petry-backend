from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..services.excel_parser import parse_report4_excel
from drf_spectacular.utils import extend_schema
import subprocess

@extend_schema(tags=["Report 4"])
class Report4UploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            subprocess.run(['python', 'scripts/download_report4.py'], check=True)
            parse_report4_excel('downloads/report4.xlsx')
            return Response({'detail': 'Отчёт успешно загружен и сохранён в БД.'})
        except Exception as e:
            return Response({'error': str(e)}, status=500)