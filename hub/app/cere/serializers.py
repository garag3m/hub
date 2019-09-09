from rest_framework import serializers

from . import models

class  AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Address
        fields = ('pk','city', 'neighborhood', 'street', 'number', 'cep', 'state')

        
# Company serializer
# - - - - - - - - - - - - - - - - - - -
class CompanySerializer(serializers.ModelSerializer):

    pk = serializers.UUIDField(read_only=True)
    address = AddressSerializer()

    def create(self, validated_data):
        address = models.Address()
        company_address = validated_data.pop('address')
        address.city = company_address['city']
        address.neighborhood= company_address['neighborhood']
        address.street= company_address['street']
        address.number= company_address['number']
        address.cep= company_address['cep']
        address.state= company_address['state']
        address.save()
        validated_data['address'] = address
        company = models.Company.objects.create(**validated_data)

        return CompanySerializer(company).data

    class Meta:
        model = models.Company
        fields = ('pk', 'name', 'cnpj', 'address', 'owner', 'agreement_number', 'cpf_owner')


class  Document_opinionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Document_opinion
        fields = ('pk','formated_date', 'process_number', 'status_name', 'company_name', 'date', 'status', 'company')


class  StageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Stage
        fields = ('pk','company_name', 'advisor', 'supervisor', 'sector', 'start_date', 'end_date','week_hours','total_hours','days','begins','ends','document_secure','support')
