from huey import crontab
from huey.contrib.djhuey import task
from app.cere import models
from docxtpl import DocxTemplate
from hub.settings import BASE_DIR
import os

@task()
def commitment_term(instance):
    commit_term = instance

    doc = DocxTemplate(os.path.join(
            BASE_DIR, 'media/documents/cere/Termo_de_Compromisso.docx'))

    context = {
        'company_name' : commit_term.company.name,
        'address_street' : commit_term.company.address.street,
        'address_number' :commit_term.company.address.number,
        'address_cep' : commit_term.company.address.cep,
        'address_city' : commit_term.company.address.city,
        'address_state' : commit_term.company.address.state,
        'company_cnpj' : commit_term.company.cnpj,
        'student_name' : commit_term.student.name,
        'student_registration': commit_term.student.registration,
        'week_hours' : commit_term.week_hours,
        'begins' : commit_term.begins,
        'ends' : commit_term.ends,
        'days' : commit_term.days,
        'supervisor' : commit_term.supervisor,
        'advisor' : commit_term.advisor,
        'support' : commit_term.support_label,
        'document_secure' : commit_term.document_secure,
        'total_hours' : commit_term.total_hours,
        'start_date' : commit_term.start_date,
        'end_date' : commit_term.end_date,
    }

    doc.render(context)
    doc.save("media/documents/cere/generated/Termo_de_Compromisso_new.docx")


@task()
def document_opinion(instance):
    doc_opinion = instance

    doc = DocxTemplate(os.path.join(
        BASE_DIR, 'media/documents/cere/parecer.docx'))

    context = {
        'document_opinion_process_number' : doc_opinion.process_number,
        'company_name' : doc_opinion.company.name,
        'document_opinion_date ' : doc_opinion.formated_date,
        'document_opnion_status' : doc_opinion.status_name,
    }
    doc.render(context)
    doc.save("media/documents/cere/generated/parecer_new.doc")


@task()
def agreement(instance):
    company = instance

    doc = DocxTemplate(os.path.join(
        BASE_DIR, 'media/documents/cere/convenio.docx'))
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
    doc.save("media/documents/cere/generated/convenio_new.docx")
