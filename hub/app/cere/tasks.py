from huey import crontab
from huey.contrib.djhuey import task
from app.cere import models
from docxtpl import DocxTemplate
from hub.settings import BASE_DIR
import os

# @task()
# def commitment_term():
# company = models.Company.objects.all()
# address = models.Address.objects.all()
# student = models.
# doc = DocxTemplate('documents/cere/Termo_de_Compromisso.doc')
# context = {
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
# }
# doc.render(context)
# doc.save("Termo_de_Compromisso_new.docx")


@task()
def document_opinion(instance):
    doc_opinion = instance

    doc = DocxTemplate(os.path.join(
        BASE_DIR, 'media\documents\cere\parecer.docx'))

    context = {
        'document_opinion_process_number' : doc_opinion.process_number,
        'company_name' : doc_opinion.company.name,
        'document_opinion_date ' : doc_opinion.formated_date,
        'document_opnion_status' : doc_opinion.status_name,
    }
    doc.render(context)
    doc.save("media\documents\cere\generated\parecer_new.doc")


@task()
def agreement(instance):
    company = instance

    doc = DocxTemplate(os.path.join(
        BASE_DIR, 'media\documents\cere\convenio.docx'))
    context = {
        'agreement_number': company.agreement_number,
        'owner': company.owner,
        'company_name': company.name,
        'address_street': company.address.street,
        'address_number': company.address.number,
        'address_cep': company.address.cep,
        'address_city': company.address.city,
        'address_state': company.address.state,
        'neighborhood': company.address.neighborhood,
        'company_cnpj': company.cnpj,
        'cpf_owner': company.cpf_owner,
    }
    doc.render(context)
    doc.save("media\documents\cere\generated\convenio_new.docx")
