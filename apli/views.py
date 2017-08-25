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
from .forms import UserForm, ClientCreateForm
from .utils import render_to_pdf # PDF
from .models import Client, Person, Project
from django.http import HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives


def update(request):
    return render(request, 'apli/update.html')


def unsubscribe(request):
    return render(request, 'apli/unsubscribe.html')


def prueba_email(request):
    return render(request, 'apli/prueba.html')


def view_prueba_email(request):
    return render(request, 'apli/vista_mail.html')


def SubscrptionView(request):
    subject, from_email, to = 'hello', 'base.EMAIL_HOST_USER', 'ismaelsorucoi@gmail.com'
    text_content = 'This is an important message.'
    htmly = get_template('apli/prueba.html')
    html_content = htmly.render()
    msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return render(request, 'apli/ingreso.html', {})


# test pdf
class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, id=kwargs['pk'])
        template = get_template('invoice.html')
        context = {"project": project, }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
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
    return render(request, 'apli/index_client.html', {'all_clients': all_clients})


@login_required(login_url='/register/login/')
def index_model(request):
    all_models = Person.objects.all()
    return render(request, 'apli/index_model.html', {'all_models': all_models})


@login_required(login_url='/register/login/')
def index_project(request):
    all_projects = Project.objects.all()
    return render(request, 'apli/index_project.html', {'all_projects': all_projects})


@login_required(login_url='/register/login/')
def index_angebot(request):
    all_projects = Project.objects.all().filter(sort='angebot')
    return render(request, 'apli/index_project.html', {'all_projects': all_projects})


@login_required(login_url='/register/login/')
def index_aufttrag(request):
    all_projects = Project.objects.all().filter(sort='aufttrag')
    return render(request, 'apli/index_project.html', {'all_projects': all_projects})


@login_required(login_url='/register/login/')
def index_job(request):
    all_projects = Project.objects.all().filter(sort='job')
    return render(request, 'apli/index_project.html', {'all_projects': all_projects})


@login_required(login_url='/register/login/')
def detail_client(request, pk):
    client = get_object_or_404(Client, id=pk)
    all_projects = client.project_set.all()
    return render(request, 'apli/detail_client.html', {'client': client, 'all_projects': all_projects})


@login_required(login_url='/register/login/')
def detail_model(request, person_id):
    model = get_object_or_404(Person, id=person_id)
    return render(request, 'apli/detail_model.html', {'model': model})


@login_required(login_url='/register/login/')
def detail_project(request, pk):
    project = get_object_or_404(Project, id=pk)
    all_models = project.assignment_set.all()
#    all_partners = project.assignment_set.all().exclude(person.statut='mod')
    return render(request, 'apli/detail_project.html', {'project': project, 'all_models': all_models})


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

    return render(request, 'apli/busca.html', {"busca_clients": querysetClients, "busca_persons": querysetPersons, "busca_projects": querysetProjects})


@login_required(login_url='/register/login/')
def ingreso(request):
    return render(request, 'apli/ingreso.html', )


@login_required(login_url='/register/login/')
def prueba_ingreso(request):
    return render(request, 'apli/prueba_ingreso.html', )


@login_required(login_url='/register/login/')
def index_calendario(request):
    return render(request, 'apli/index_calendario.html', )


@login_required(login_url='/register/login/')
def index_cotizacion(request):
    return render(request, 'apli/index_cotizacion.html', )


@login_required(login_url='/register/login/')
def index_home_page(request):
    return render(request, 'apli/index_home_page.html', )


@login_required(login_url='/register/login/')
def index_orden_compra(request):
    return render(request, 'apli/index_orden_compra.html', )


@login_required(login_url='/register/login/')
def index_personas(request):
    return render(request, 'apli/index_personas.html', )


class ClientCreate(LoginRequiredMixin, CreateView):
    model = Client
    fields = ['name', 'name_short', 'company', 'company_short', 'country', 'city', 'zip_code', 'address', 'email', 'phone', 'comment']


class ClientUpdate(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ['name', 'name_short', 'company', 'company_short', 'country', 'city', 'zip_code', 'address', 'email', 'phone', 'comment']


class ClientDelete(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('index_client')


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
