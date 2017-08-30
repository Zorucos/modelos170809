from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy #delete
from django.http import HttpResponse #pdf
from django.template.loader import get_template #pdf
from django.template import Context
from django.views.generic import View
from django.contrib.auth.decorators import login_required # requisito login  def
from django.contrib.auth.mixins import LoginRequiredMixin # requisito login  viw 
from django.db.models import Q # busqueda
from django.core.mail import send_mail # send email
from django.contrib import messages 
from django.conf import settings # mail
from django.http import HttpResponse
from .forms import UserForm, ClientCreateForm, PersonCreateForm
from .utils import render_to_pdf # PDF
from .models import Client, Person, Project, Attachment, Assignment, Cost, Horaire
from django.http import HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from datetime import date
from django.core.files.base import ContentFile
from io import BytesIO
from xhtml2pdf import pisa


# { email testing OPEN 
def update(request):
    return render(request, 'apli/mail/update.html')


def unsubscribe(request):
    return render(request, 'apli/mail/unsubscribe.html')


def prueba_email(request):
    return render(request, 'apli/mail/prueba.html')

#tis def is only for check the email design without sending email 
def view_prueba_email(request):
    return render(request, 'apli/mail/vista_mail.html')

# what is doing this function is send an email with a a template html msg. then go to dashboard. 
def SubscrptionView(request, pk):
    project = get_object_or_404(Project, id=pk)
    context = {"project": project, }
    subject, from_email, to = 'new angebot', 'base.EMAIL_HOST_USER', project.client.email
    text_content = 'This is an important message.'
    htmly = get_template('apli/mail/prueba.html')
    html_content = htmly.render(context)
    msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return render(request, 'apli/dashboard/dashboard.html', {})

#  email testing CLOSE }

# test pdf
class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, id=kwargs['pk'])
        template = get_template('apli/pdf/invoice.html')
        context = {"project": project, }
        html = template.render(context)
        pdf = render_to_pdf('apli/pdf/invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
        if download:
            content = "attachment; filename='{Project.name} %s'" %(filename) #poner nombre de proyecto
            response['Content-Disposition'] = content

        return response
        return HttpResponse("Not found")
# test pdf

# crear view de proyeto por isma ABIR

class ClienteCreateView(LoginRequiredMixin, CreateView):
    form_class = ClientCreateForm
    login_url = '/login/'
    template_name = 'apli/form.html'
    success_url = "/apli/index_client"

    def form_valid(self, form):
            instance = form.save(commit=False)
            instance.owner = self.request.user
            return super(ClienteCreateView, self).form_valid(form)



# crar view de proyecto por isma CERRAR


# #register
# class RegisterView(CreateView):
#     form_class = RegisterForm
#     template_name = 'apli/register.html'
#     success_url = "/apli/index_contact"
# #register


@login_required(login_url='/register/login/')
def index_client(request):
    all_clients = Client.objects.all()
    return render(request, 'apli/Client/index_client.html', {'all_clients': all_clients})


@login_required(login_url='/register/login/')
def index_model(request):
    all_models = Person.objects.all().filter(statut='modell')
    return render(request, 'apli/model/index_model.html', {'all_models': all_models})

@login_required(login_url='/register/login/')
def index_person(request):
    all_models = Person.objects.all().exclude(statut='modell')
    return render(request, 'apli/person/index_person.html', {'all_models': all_models})


@login_required(login_url='/register/login/')
def index_project(request):
    all_projects = Project.objects.all()
    return render(request, 'apli/angebot/index_angebot.html', {'all_projects': all_projects})


@login_required(login_url='/register/login/')
def index_angebot(request):
    all_projects = Project.objects.all().filter(sort='Angebot')
    return render(request, 'apli/angebot/index_angebot.html', {'all_projects': all_projects})


@login_required(login_url='/register/login/')
def index_aufttrag(request):
    all_projects = Project.objects.all().filter(sort='Auftrag')
    return render(request, 'apli/auftrag/index_auftrag.html', {'all_projects': all_projects})


@login_required(login_url='/register/login/')
def index_job(request):
    all_projects = Project.objects.all().filter(sort='job')
    return render(request, 'apli/job/index_job.html', {'all_projects': all_projects})

@login_required(login_url='/register/login/')
def index_cost(request):
    all_costs = Cost.objects.all().filter(sort='')
    return render(request, 'apli/cost/index_cost.html', {'all_costs': all_costs})

@login_required(login_url='/register/login/')
def index_assignment(request):
    all_assignments = Assignment.objects.all().filter(sort='')
    return render(request, 'apli/job/index_assignments.html', {'all_assignments': all_assignments})


@login_required(login_url='/register/login/')
def detail_client(request, pk):
    client = get_object_or_404(Client, id=pk)
    all_projects = client.project_set.all()
    return render(request, 'apli/Client/detail_client.html', {'client': client, 'all_projects': all_projects})


@login_required(login_url='/register/login/')
def detail_cost(request, pk):
    cost = get_object_or_404(Cost, id=pk)
    return render(request, 'apli/cost/detail_cost.html', {'cost': cost})


@login_required(login_url='/register/login/')
def detail_model(request, pk):
    model = get_object_or_404(Person, id=pk)
    return render(request, 'apli/model/detail_model.html', {'model': model})


@login_required(login_url='/register/login/')
def detail_person(request, pk):
    model = get_object_or_404(Person, id=pk)
    return render(request, 'apli/person/detail_person.html', {'model': model})


@login_required(login_url='/register/login/')
def detail_assignment(request, pk):
    assignment = get_object_or_404(Assignment, id=pk)
    all_horaire = assignment.horaire_set.all()
    return render(request, 'apli/assignment/detail_assignment.html', {'assignment': assignment, 'all_horaire': all_horaire})


@login_required(login_url='/register/login/')
def detail_project(request, pk):
    project = get_object_or_404(Project, id=pk)
    all_models = project.assignment_set.all()
    all_attachments = project.attachment_set.all()
    all_costs = project.cost_set.all()
#    all_partners = project.assignment_set.all().exclude(person.statut='mod')
    return render(request, 'apli/angebot/detail_angebot.html', {'project': project, 'all_models': all_models, 'all_attachments': all_attachments, 'all_costs': all_costs})


@login_required(login_url='/register/login/')
def busca(request):
    query = request.GET.get("q")
    querysetClients = Client.objects.all()
    if query:
        querysetClients = querysetClients.filter(
            Q(name__icontains=query)
        ).distinct()

    querysetPersons = Person.objects.all()
    if query:
        querysetPersons = querysetPersons.filter(
            Q(name__icontains=query)|
            Q(email__icontains=query)
        ).distinct()

    querysetProjects = Project.objects.all()
    if query:
        querysetProjects = querysetProjects.filter(
            Q(name__icontains=query)
        ).distinct()

    return render(request, 'apli/busca/busca.html', {"busca_clients": querysetClients, "busca_persons": querysetPersons, "busca_projects": querysetProjects})


@login_required(login_url='/register/login/')
def dashboard(request):
    return render(request, 'apli/dashboard/dashboard.html', )


@login_required(login_url='/register/login/')
def prueba_ingreso(request):
    return render(request, 'apli/prueba_ingreso.html', )




# @login_required(login_url='/register/login/')
# def index_angebot(request):
#     return render(request, 'apli/angebot/index_angebot.html', )


@login_required(login_url='/register/login/')
def index_home_page(request):
    return render(request, 'apli/index_home_page.html', )


@login_required(login_url='/register/login/')
def index_orden_compra(request):
    return render(request, 'apli/index_orden_compra.html', )


# @login_required(login_url='/register/login/')
# def index_person(request):
#     return render(request, 'apli/person/index_person.html', )


class ClientCreate(LoginRequiredMixin, CreateView):
    model = Client
    fields = ['name', 'name_short', 'company', 'company_short', 'country', 'city', 'zip_code', 'address', 'email', 'phone', 'comment']


class ClientUpdate(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ['name', 'name_short', 'company', 'company_short', 'country', 'city', 'zip_code', 'address', 'email', 'phone', 'comment']


class ClientDelete(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('index_client')





class PersonCreate(LoginRequiredMixin, CreateView):
    model = Person
    fields = ['name', 'name_short', 'company', 'company_short', 'agent', 'agent_short', 'country', 'city', 'zip_code', 'address', 'email', 'phone','email','sedcard','statut','comment','bank_account', 'website']


class PersonUpdate(LoginRequiredMixin, UpdateView):
    model = Person
    fields = ['name', 'name_short', 'company', 'company_short', 'agent', 'agent_short', 'country', 'city', 'zip_code', 'address', 'email', 'phone','email','sedcard','statut','comment','bank_account', 'website']


class PersonDelete(LoginRequiredMixin, DeleteView):
    model = Person
    success_url = reverse_lazy('index_person')

# crear, nueva info y delete assignment

class AssignmentCreate(LoginRequiredMixin, CreateView):
    model = Assignment

    fields = ['project', 'person', 'model_type', 'travel_cost', 'hotel_cost', 'other_cost', 'comment_WG', 'statut', 'send_date', 'payment_date', 'total_price']
class AssignmentUpdate(LoginRequiredMixin, UpdateView):
    model = Assignment
    fields = ['project', 'person', 'model_type', 'travel_cost', 'hotel_cost', 'other_cost', 'comment_WG', 'statut', 'send_date', 'payment_date', 'total_price']


class AssignmentDelete(LoginRequiredMixin, DeleteView):
    model = Assignment
    success_url = reverse_lazy('index_assignment')

class CostCreate(LoginRequiredMixin, CreateView):
    model = Cost
    fields = ['user', 'project', 'comment', 'date', 'amount', 'title', 'statut']

class CostUpdate(LoginRequiredMixin, UpdateView):
    model = Cost
    fields = ['user', 'project', 'comment', 'date', 'amount', 'title', 'statut']


class CostDelete(LoginRequiredMixin, DeleteView):
    model = Cost
    success_url = reverse_lazy('index_cost')


    

# crear, nueva info y delete proyecto
class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['name', 'client', 'start', 'finish', 'user', 'comment', 'sort', 'all_day', 'half_day', 'half_day_price_pro', 'all_day_price_pro', 'over_price_pro', 'all_in_price_pro', 'half_day_price_semipro', 'all_day_price_semipro', 'over_price_semipro', 'all_in_price_semipro', 'country', 'city', 'zip_code', 'address', 'comment_address', 'honorary_base', 'honorary_plus', 'quantity_models_honorary_plus', 'ms_price', 'ms_hours', 'requirement_price', 'requirement_hours', 'requisiten_price_for_each_model', 'other_title', 'other_description', 'other_price', 'other_hours', 'photo_price', 'photo_hours', 'tax']


class ProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['name', 'client', 'start', 'finish', 'user', 'comment', 'sort', 'all_day', 'half_day', 'half_day_price_pro', 'all_day_price_pro', 'over_price_pro', 'all_in_price_pro', 'half_day_price_semipro', 'all_day_price_semipro', 'over_price_semipro', 'all_in_price_semipro', 'country', 'city', 'zip_code', 'address', 'comment_address', 'honorary_base', 'honorary_plus', 'quantity_models_honorary_plus', 'ms_price', 'ms_hours', 'requirement_price', 'requirement_hours', 'requisiten_price_for_each_model', 'other_title', 'other_description', 'other_price', 'other_hours', 'photo_price', 'photo_hours', 'tax']


class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('index_project')


# HOARIO
class HoraireCreate(LoginRequiredMixin, CreateView):
    model = Horaire
    fields = ['assignment', 'date', 'start_time', 'finish_time']


class HoraireUpdate(LoginRequiredMixin, UpdateView):
    model = Horaire
    fields = ['assignment', 'date', 'start_time', 'finish_time']


class HoraireDelete(LoginRequiredMixin, DeleteView):
    model = Horaire
    success_url = reverse_lazy('index_project')

def project_send(request, pk):
    project = get_object_or_404(Project, id=pk)
    all_models = project.assignment_set.all()
    all_attachments = project.attachment_set.all()
    all_costs = project.cost_set.all()

    # debo crear el attachment
    template = get_template('apli/pdf/invoice.html')
    context = {"project": project, }
    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)

    at = Attachment(project=project, sort=project.sort, send_date = date.today())

    at.file.save('nombre.pdf', ContentFile(result.getvalue()))
    at.save()

    context2 = {"project": project, }
    subject, from_email, to = 'new angebot', 'base.EMAIL_HOST_USER', project.client.email
    text_content = 'This is an important message.'
    htmly = get_template('apli/mail/prueba.html')
    html_content = htmly.render(context2)
    msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.attach(at.file.name, result.getvalue(), )
    msg.send()
    return render(request, 'apli/angebot/detail_angebot.html', {'project': project, 'all_models': all_models, 'all_attachments': all_attachments, 'all_costs': all_costs})



