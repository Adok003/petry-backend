from django.db import models

class Report4(models.Model):
    proceeding_id = models.CharField(max_length=100)
    issuer = models.CharField(max_length=255, blank=True, null=True)
    judge = models.CharField(max_length=255, blank=True, null=True)
    case_number = models.CharField(max_length=100)
    case_status = models.CharField(max_length=100)
    date_started = models.DateField(null=True, blank=True)
    date_closed = models.DateField(null=True, blank=True)
    debtor = models.CharField(max_length=255)
    claimant = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    category = models.CharField(max_length=100, blank=True)
    document_type = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100, blank=True)
    period_of_request = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)