from django.core import serializers

with open("BRCA_data_converted.json", "w") as out:
    json_serializer.serialize(SomeModel.objects.all(), stream=out)

manage.py dumpdata 
dashboard.Patient 
dashboard.Sequencing 
dashboard.Gene 
dashboard.Variant --output=dashboard/fixtures/data.json