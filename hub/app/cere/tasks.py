from huey import crontab
from huey.contrib.djhuey import task
from app.cere import models
from docxtpl import DocxTemplate

#@task()
#def commitment_term():
   # company = models.Company.objects.all()
   # address = models.Address.objects.all()
    #student = models.
    #doc = DocxTemplate('documents/cere/Termo_de_Compromisso.doc')
    #context = { 
    #   'company_name' : company_name,
    #    'address_street' : address_street,
     #   'address_number' :address_number,
      #  'address_cep' : address_cep,
     #   'address_city' : address_city,
     #   'address_state' : address_state,
     #   'company_cnpj' : company_cnpj,
     #   'student_name' : student_name,
     #   'student_registration': student_registration,
      #  'week_hours' : week_hours,
    #    'begins' : begins,
     #   'ends' : ends,
    #    'days' : days,
     #   'supervisor' : supervisor,
     #   'advisor' : advisor,
   #     'support' : support,
     #   'document_secure' : document_secure,
    #    'total_hours' : total_hours,
    #    'start_date' : start_date,
    #    'end_date' : end_date,
    #}
    #doc.render(context)
    #doc.save("Termo_de_Compromisso_new.docx")

#@task()
#def document_opinion():
 #   company = models.Company.objects.all()
  #  address = models.Address.objects.all()
    #student = models.
   # doc = DocxTemplate('documents/cere/Parecer.doc')
    #context = { 
     #   'document_opinion_process_number' : document_opinion_process_number
      #  'company_name' : company_name,
       # 'document_opinion_date ' : document_opinion_date ,
        #'document_opnion_status' : document_opnion_status,
   # }
    #doc.render(context)
    #doc.save("parecer_new.docx")

    
@task()
def agreement():
    company = models.Company.objects.all()
    address = models.Address.objects.all()

    doc = DocxTemplate('/home/ifpb/Área de Trabalho/Projetos Adriel/hub/hub/media/documents/cere/Convênio.docx')
    context = { 
        'agreement_number': company.agreement_number,
        'owner' : company.owner,
        'company_name' : company.name,
        'address_street' : address.street,
        'address_number' :address.number,
        'address_cep' : address.cep,
        'address_city' : address.city,
        'address_state' : address.state,
        'company_cnpj' : company.cnpj,
        'cpf_owner': company.cpf_owner,
    }
    doc.render(context)
    doc.save("Convênio_new.docx")