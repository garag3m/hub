from rest_framework import serializers

from . import models

class  AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Address
        fields = ('pk','city', 'neighborhood', 'street', 'number', 'cep', 'state')

        
# Company serializer
# - - - - - - - - - - - - - - - - - - -
class CompanySerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = models.Company
        fields = ('pk', 'name', 'cnpj', 'address', 'owner', 'agreement_number', 'cpf_owner')


class  Document_opinionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Document_opinion
        fields = ('pk','date', 'process_number', 'status', 'company')


class  StageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Stage
        fields = ('pk','company', 'advisor', 'supervisor', 'sector', 'start_date', 'end_date','week_hours','total_hours','days','begins','ends','document_secure','support')
