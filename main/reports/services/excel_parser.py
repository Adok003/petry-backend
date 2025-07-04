import pandas as pd
from ..models import Report4

def parse_report4_excel(file_path):
    df = pd.read_excel(file_path)

    for _, row in df.iterrows():
        Report4.objects.create(
            proceeding_id=row.get('Proceeding ID'),
            issuer=row.get('Орган выдающий исполнительный документ'),
            judge=row.get('Судебный исполнитель'),
            case_number=row.get('№ производства'),
            case_status=row.get('Статус производства'),
            date_started=row.get('Дата возбуждения'),
            date_closed=row.get('Дата закрытия'),
            debtor=row.get('Должник'),
            claimant=row.get('Взыскатель'),
            amount=row.get('Сумма'),
            category=row.get('Категория'),
            document_type=row.get('Вид документа'),
            status=row.get('Status'),
            period_of_request=row.get('PeriodOfRequest'),
        )
