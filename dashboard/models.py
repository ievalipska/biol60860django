from django.conf import settings
from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords

class Variants(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Age = models.IntegerField(null=True, blank=True)
    Stage = models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=50, null=True, blank=True)
    Sequencer = models.CharField(max_length=100, null=True, blank=True)
    cDNA_variant = models.CharField(max_length=100, null=True, blank=True)
    protein_variant = models.CharField(max_length=100, null=True, blank=True)
    genomic_variant = models.CharField(max_length=100, null=True, blank=True)
    Gene = models.CharField(max_length=50, null=True, blank=True)
    Classification = models.CharField(max_length=50, null=True, blank=True)
    history = HistoricalRecords()
    
    def __str__(self):
        return self.Name
