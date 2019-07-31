from rest_framework import viewsets, permissions
from django.db.models import Q
from . import models, serializers

class CompanyViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.CompanySerializer

    def get_queryset(self):
        search = self.request.query_params.get('search', None)
        name = self.request.query_params.get('name', None)
        cnpj = self.request.query_params.get('cnpj', None)
        Address = self.request.query_params.get('Address', None)
        owner = self.request.query_params.get('owner', None)
        agreement_number = self.request.query_params.get('agreement_number', None)
        cpf_owner = self.request.query_params.get('cpf_owner', None)
        queryset = models.Company.objects.all()

        if search:
            agreement_number = self.request.query_params.get('agreement_number', None)
            queryset = queryset.filter(Q(name=search) | Q(cnpj=search) | Q(Address=search) | Q(owner=search) | Q(agreement_number=search) | Q(cpf_owner=search))
        else:
            if name:
                queryset = queryset.filter(name=name)
            if cnpj:
                queryset = queryset.filter(cnpj=cnpj)
            if Address:
                queryset = queryset.filter(Address=Address)
            if owner:
                queryset = queryset.filter(owner=owner)
            if agreement_number:
                queryset = queryset.filter(agreement_number=agreement_number)
            if cpf_owner:
                queryset = queryset.filter(cpf_owner=cpf_owner)
            return queryset


class Document_opinionViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.Document_opinionSerializer

    def get_queryset(self):
        search = self.request.query_params.get('search', None)
        date = self.request.query_params.get('date', None)
        process_number = self.request.query_params.get('process_number', None)
        status = self.request.query_params.get('status', None)
        company =  self.request.query_params.get('Company', None)
        queryset = models.Document_opinion.objects.all()

        if search:
            process_number = self.request.query_params.get('process_number', None)
            queryset = queryset.filter(Q(date=search) | Q(process=search) | Q(status=search) | Q(company=search))
        else:
            if date:
                queryset = queryset.filter(date=date)
            if process_number:
                queryset = queryset.filter(process_number=process)
            if status:
                queryset = queryset.filter(status= status)
            if company:
                queryset = queryset.filter(company=company)
            return queryset


class AddressViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.AddressSerializer 

    def get_queryset(self):
        search = self.request.query_params.get('search', None)
        city= self.request.query_params.get('city', None)
        neighborhood = self.request.query_params.get('neighborhood', None)
        street = self.request.query_params.get('street', None)
        number =  self.request.query_params.get('number', None)
        cep =  self.request.query_params.get('cep', None)
        state =  self.request.query_params.get('state', None)
        queryset = models.Address.objects.all()

        if search:
            process_number = self.request.query_params.get('city', None)
            queryset = queryset.filter(Q(city=search) | Q(neighborhood=search) | Q(state=search) | Q(cep=search) | Q(number=search) | Q(street=search))
        else:
            if city:
                queryset = queryset.filter(city=city)
            if neighborhood:
                queryset = queryset.filter(neighborhood=neighborhood)
            if street :
                queryset = queryset.filter(street = street)
            if  number:
                queryset = queryset.filter( number= number)
            if cep:
                 queryset = queryset.filter(cep=cep)
            if  state:
                queryset = queryset.filter( state= state)  
        return queryset        

class StageViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.StageSerializer

    def get_queryset(self):
        search = self.request.query_params.get('search', None)
        company = self.request.query_params.get('company', None)
        advisor = self.request.query_params.get('advisor', None)
        supervisor = self.request.query_params.get('supervisor', None)
        sector = self.request.query_params.get('sector', None)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        week_hours = self.request.query_params.get('week_hours', None)
        total_hours = self.request.query_params.get('total_hours', None)
        days = self.request.query_params.get('days', None)
        begins= self.request.query_params.get('begins', None)
        ends = self.request.query_params.get('ends', None)
        support= self.request.query_params.get('support', None)
        document_secure = self.request.query_params.get('document_secure', None)
        support = self.request.query_params.get('support', None)
        queryset = models.Stage.objects.all()

        if search:
            agreement_number = self.request.query_params.get('agreement_number', None)
            queryset = queryset.filter(Q(company=search) | Q(advisor=search) | Q(sector=search) | Q(start_date=search) | Q(end_date=search) | Q(week_hours=search) | Q(total_hours=search) | Q(days=search) | Q(begins=search) | Q(ends=search) | Q(support=search) | Q(document_secure=search))
        else:
            if company:
                queryset = queryset.filter(company=company)
            if advisor:
                queryset = queryset.filter(advisor=advisor)
            if supervisor:
                queryset = queryset.filter(supervisor=advisor)
            if sector:
                queryset = queryset.filter(sector=sector)
            if start_date:
                queryset = queryset.filter(start_date=start_date)
            if end_date:
                queryset = queryset.filter(end_date=end_date)
            if week_hours:
                queryset = queryset.filter(week_hours=week_hours)
            if total_hours:
                queryset = queryset.filter(total_hours=total_hours)
            if days:
                queryset = queryset.filter(days=days)
            if begins:
                queryset = queryset.filter(begins=begins)
            if ends:
                queryset = queryset.filter(ends=ends)
            if support:
                queryset = queryset.filter(support=support)
            if document_secure:
                queryset = queryset.filter(document_secure=document_secure)
            return queryset        
