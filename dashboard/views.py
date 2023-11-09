from django.shortcuts import render
from .models import Variants
from django.http import JsonResponse
import json

def home(request):
    return filtered(request)
    
def filtered(request, column=None, filter=None):
    #Use column and filter to narrow down list of variants that are returned. CASE SENSITIVE.


    
    variants = Variants.objects.all()
    #if column=="Name":
        #variants = [v for v in variants if filter in v.Name]
    if column == "Name":
        variants = [v for v in variants if str(filter).lower() in str(v.Name).lower()]
        print(variants)
    

        #Copy paste for all fields. Int should be different?
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


