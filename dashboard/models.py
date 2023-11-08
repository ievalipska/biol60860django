from django.conf import settings
from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Age = models.IntegerField(null=True, blank=True)
    history = HistoricalRecords()

class Sequencing_Run(models.Model):
    id = models.AutoField(primary_key=True)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Sequencer = models.CharField(max_length=100, null=True, blank=True)
    history = HistoricalRecords()
    
class Gene(models.Model):
    id = models.AutoField(primary_key=True)
    Gene_Symbol = models.CharField(max_length=50, null=True, blank=True)
    history = HistoricalRecords()

class Variant(models.Model):
    id = models.AutoField(primary_key=True)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Sequencing_Run = models.ForeignKey(Sequencing_Run, on_delete=models.CASCADE)
    Gene = models.ForeignKey(Gene, on_delete=models.CASCADE)
    genomic_variant = models.CharField(max_length=100, null=True, blank=True)
    cDNA_variant = models.CharField(max_length=100, null=True, blank=True)
    protein_variant = models.CharField(max_length=100, null=True, blank=True)
    Classification = models.CharField(max_length=100, null=True, blank=True)
    history = HistoricalRecords()

class Disease(models.Model):
    id = models.AutoField(primary_key=True)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    Stage = models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=50, null=True, blank=True)
    history = HistoricalRecords()
