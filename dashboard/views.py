from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.http import JsonResponse
from .models import Variants
import json

def home(request):
    return filtered(request)
    
def filtered(request, column=None, filter=None):
    #Use column and filter to narrow down list of variants that are returned. Modified to be case insensitive.

    variants = Variants.objects.all()
    
    if column == "Name":
        variants = [v for v in variants if str(filter).lower() in str(v.Name).lower()]
    if column=="Age":
        variants = [v for v in variants if int(filter)==int(v.Age)]
    if column=="Stage":
        variants = [v for v in variants if int(filter)==int(v.Stage)]
    if column == "Description":
        variants = [v for v in variants if str(filter).lower() in str(v.Description).lower()]
    if column == "Sequencer":
        variants = [v for v in variants if str(filter).lower() in str(v.Sequencer).lower()] 
    if column == "Gene":
        variants = [v for v in variants if str(filter).lower() in str(v.Gene).lower()]
    if column == "cDNA_variant":
        variants = [v for v in variants if str(filter).lower() in str(v.cDNA_variant).lower()]
    if column == "protein_variant":
        variants = [v for v in variants if str(filter).lower() in str(v.protein_variant).lower()]
    if column == "genomic_variant":
        variants = [v for v in variants if str(filter).lower() in str(v.genomic_variant).lower()]
    if column == "Classification":
        variants = [v for v in variants if str(filter).lower() in str(v.Classification).lower()]

    
    return render(request, 'dashboard/home.html', {'variants': variants})


def addvariant(request):
    return render(request, 'dashboard/addvariant.html')


def createvariant(request):
    insert = json.loads(request.body)
    
    #Returns an error if not all fields are set. Mandates integer use for Age and Stage.
    check_fields = (
        "Name" in insert and len(insert["Name"]) > 0
        and "Age" in insert and type(insert["Age"]) is int
        and "Stage" in insert and type(insert["Stage"]) is int
        and "Description" in insert and len(insert["Description"]) > 0
        and "Sequencer" in insert and len(insert["Sequencer"]) > 0
        and "Gene" in insert and len(insert["Gene"]) > 0
        and "cDNA_variant" in insert and len(insert["cDNA_variant"]) > 0
        and "protein_variant" in insert and len(insert["protein_variant"]) > 0
        and "genomic_variant" in insert and len(insert["genomic_variant"]) > 0
        and "Classification" in insert and len(insert["Classification"]) > 0
    )

    if not check_fields:
        return JsonResponse({
            "error": "Not all fields are set."
        }) 
    
    #Insert into database.
    Variants(**insert).save()
    
    return JsonResponse(insert)


def editvariant(request, pk):
    if request.method == 'POST':
        try:
            instance = get_object_or_404(Variants, pk=pk)
            
            instance.Name = request.POST.get('Name')
            instance.Age = request.POST.get('Age')
            instance.Stage = request.POST.get('Stage')
            instance.Description = request.POST.get('Description')
            instance.Sequencer = request.POST.get('Sequencer')
            instance.Gene = request.POST.get('Gene')
            instance.cDNA_variant = request.POST.get('cDNA_variant')
            instance.protein_variant = request.POST.get('protein_variant')
            instance.genomic_variant = request.POST.get('genomic_variant')
            instance.Classification = request.POST.get('Classification')
            
            instance.save()
            return redirect('home')
        
        except Exception as e:
            print(e)
            return JsonResponse({'status': 'error'})
    
    else:
        return JsonResponse({'status': 'error'})
    
    
def summary(request):
    # Get data for summary statistics
    total_items = Variants.objects.count()
    unique_patients = Variants.objects.values('Name').distinct().count()
    total_genes = Variants.objects.values('Gene').distinct().count()
    
    data = {
        'total_items': total_items,
        'unique_patients': unique_patients,
        'total_genes': total_genes,
    }
    
    return render(request, 'dashboard/summary.html', data)


