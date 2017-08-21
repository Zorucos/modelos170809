from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy #delete
from django.http import HttpResponse #pdf
from django.template.loader import get_template #pdf
from django.template import Context
from django.views.generic import View
from django.contrib.auth.decorators import login_required # requisito login  def
from django.contrib.auth.mixins import LoginRequiredMixin # requisito login  viw 
from django.db.models import Q #busqueda
from django.core.mail import send_mail #send email
from django.contrib import messages 
from django.conf import settings #mail
from django.http import HttpResponse
from .forms import UserForm, ClientCreateForm
from .utils import render_to_pdf #PDF
from .models import Client, Persona, Proyecto
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


#skdjaksdgkasgkads

def SubscrptionView(request):
    # print ("email sent")
    # html_content = '<p>This is an <strong>important</strong> message.</p>'
    # send_mail('probando probando', html_content, 'base.EMAIL_HOST_USER', ['ismaelsorucoi@gmail.com'], fail_silently=False,)
    # messages.success(request, 'Gracias por registrarte')
    # return render(request, 'apli/ingreso.html', {})
    subject, from_email, to = 'hello', 'base.EMAIL_HOST_USER', 'ismaelsorucoi@gmail.com'
    text_content = 'This is an important message.'
    htmly = get_template('apli/prueba.html') 
    
    html_content = htmly.render()
    #'<html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /><title></title><style></style></head><body><table border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" id="bodyTable"><tr><td align="center" valign="top"><table border="0" cellpadding="20" cellspacing="0" width="600" id="emailContainer"><tr><td align="center" valign="top" font-size="x-large"><p><strong>We have the solution for you</strong></p></td></tr><img src="http://www.hainke.de/res/images/HAINKE-Hauptlogo.svg?m=1457700739" /></table></td></tr></table></body><table border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" id="bodyTable"><tr><td align="center" valign="top"><table border="0" cellpadding="20" cellspacing="0" width="600" id="emailContainer"><tr><td align="center" valign="top"><table border="0" cellpadding="20" cellspacing="0" width="100%" id="emailHeader"><tr><td align="center" valign="top">Im Laufe eines industriellen Produktionsprozesses entstehen Stäube, Gase und Dämpfe, die unangenehm oder gar schädlich sein können. Ob bei der Rohstoffverarbeitung, der Herstellung oder dem Handling – wurden diese Emissionen erst einmal freigesetzt, müssen sie erfasst und gefiltert werden. Darin sind wir Experten.HAINKE FILTERANLAGEN entwickelt innovative und kundenspezifische Lösungen für die Erfassung und die Reinigung der belasteten Luft. Unser oberstes Ziel: Menschen, Maschinen und die Umwelt zu schützen.Was uns von anderen Anbietern unterscheidet? Unsere jahrzehntelange Erfahrung, höchste Qualität bei Produkten, Anlagen und den zugehörigen Dienstleistungen sowie ein fester und kompetenter Mitarbeiterstamm. Wir beliefern Anlagenbauer und Endkunden der gesamten Industrie. Auf unsere Kompetenz vertrauen Marktführer unter anderem in der Futter- und der Lebensmittelbranche. Produkte und Anlagen von HAINKE werden weltweit genutzt und mittlerweile in alle Kontinente geliefert.</td></tr></table></td></tr><tr><td align="center" valign="top"><table border="0" cellpadding="20" cellspacing="0" width="100%" id="emailBody"><tr><td align="center" valign="top"><!-- This is where my body content goes. --><table border="0" cellpadding="0" cellspacing="0" width="600" id="templateColumns"><tr><td align="center" valign="top" width="33%" class="templateColumnContainer"><table border="0" cellpadding="10" cellspacing="0" width="100%"><tr><td class="leftColumnContent"><img src="http://placekitten.com/g/180/200" class="columnImage" /></td></tr><tr><td valign="top" class="leftColumnContent"><h2>Design bei uns</h2>Lorem ipsum dolor sit amet.</td></tr></table></td><td align="center" valign="top" width="33%" class="templateColumnContainer"><table border="0" cellpadding="10" cellspacing="0" width="100%"><tr><td class="centerColumnContent"><img src="http://placekitten.com/g/180/200" class="columnImage" /></td></tr><tr><td valign="top" class="centerColumnContent"><h2>Lösungs be uns</h2>Lorem ipsum dolor sit amet.</td></tr></table></td><td align="center" valign="top" width="33%" class="templateColumnContainer"><table border="0" cellpadding="10" cellspacing="0" width="100%"><tr><td class="rightColumnContent"><img src="http://www.hainke.de/_thumbnails_/287_1_Hainke-Filteranlagen-Futterindustrie-135424277.jpg?m=1457700753"  height="200" width="190" class="columnImage" /></td></tr><tr><td valign="top" class="rightColumnContent"><h2>preche mit uns</h2>Lorem ipsum dolor sit amet.</td></tr></table></td></tr></table></td></tr></table></td></tr></table></td></tr></table><table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color:#505050; border:1px solid #353535; border-radius:5px;"><tr><td align="center" valign="middle" style="color:#FFFFFF; font-family:Helvetica, Arial, sans-serif; font-size:16px; font-weight:bold; letter-spacing:-.5px; line-height:150%; padding-top:15px; padding-right:30px; padding-bottom:15px; padding-left:30px;"><a href="http://www.hainke.de" target="_blank" style="color:#FFFFFF; text-decoration:none;">CONTACT HAINKE FILTERANLAGEN GmgH</a></td></tr></table><table border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" id="bodyTable"><tr><td align="center" valign="top"><table border="0" cellpadding="20" cellspacing="0" width="600" id="emailContainer"><tr><td align="center" valign="top" font-size="x-large"><p><strong>An der Imbäke 727798 Hude</strong></p>Postfach 12 48 / 27795 Hude / Telefon:    +49 4408 8077-0 / Telefax:    +49 4408 8077-10 / Internet:     www.hainke.de / E-Mail:       info@hainke.de</td></tr></table></td></tr></table>'
    #'<html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /><title></title><style></style></head><body><table border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" id="bodyTable"><tr><td align="center" valign="top"><table border="0" cellpadding="20" cellspacing="0" width="600" id="emailContainer"><tr><td align="center" valign="top" font-size="x-large"><p><strong>We have the solution for you</strong></p></td></tr><img src="http://www.hainke.de/res/images/HAINKE-Hauptlogo.svg?m=1457700739" height= 200 max-width: 200/></table></td></tr></table></body><table border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" id="bodyTable"><tr><td align="center" valign="top"><table border="0" cellpadding="20" cellspacing="0" width="600" id="emailContainer"><tr><td align="center" valign="top"><table border="0" cellpadding="20" cellspacing="0" width="100%" id="emailHeader"><tr><td align="center" valign="top">Im Laufe eines industriellen Produktionsprozesses entstehen Stäube, Gase und Dämpfe, die unangenehm oder gar schädlich sein können. Ob bei der Rohstoffverarbeitung, der Herstellung oder dem Handling – wurden diese Emissionen erst einmal freigesetzt, müssen sie erfasst und gefiltert werden. Darin sind wir Experten. HAINKE FILTERANLAGEN entwickelt innovative und kundenspezifische Lösungen für die Erfassung und die Reinigung der belasteten Luft. Unser oberstes Ziel: Menschen, Maschinen und die Umwelt zu schützen. Was uns von anderen Anbietern unterscheidet? Unsere jahrzehntelange Erfahrung, höchste Qualität bei Produkten, Anlagen und den zugehörigen Dienstleistungen sowie ein fester und kompetenter Mitarbeiterstamm. Wir beliefern Anlagenbauer und Endkunden der gesamten Industrie. Auf unsere Kompetenz vertrauen Marktführer unter anderem in der Futter- und der Lebensmittelbranche. Produkte und Anlagen von HAINKE werden weltweit genutzt und mittlerweile in alle Kontinente geliefert.</td></tr></table></td></tr><tr><td align="center" valign="top"><table border="0" cellpadding="20" cellspacing="0" width="100%" id="emailBody"><tr><td align="center" valign="top"><!-- This is where my body content goes. --><table border="0" cellpadding="0" cellspacing="0" width="600" id="templateColumns"><tr><td align="center" valign="top" width="33%" class="templateColumnContainer"><table border="0" cellpadding="10" cellspacing="0" width="100%"><tr><td class="leftColumnContent"><img src="http://placekitten.com/g/180/200" class="columnImage" /></td></tr><tr><td valign="top" class="leftColumnContent"><h2>Design bei uns</h2>Lorem ipsum dolor sit amet.</td></tr></table></td><td align="center" valign="top" width="33%" class="templateColumnContainer"><table border="0" cellpadding="10" cellspacing="0" width="100%"><tr><td class="centerColumnContent"><img src="http://placekitten.com/g/180/200" class="columnImage" /></td></tr><tr><td valign="top" class="centerColumnContent"><h2>Lösungs be uns</h2>Lorem ipsum dolor sit amet.</td></tr></table></td><td align="center" valign="top" width="33%" class="templateColumnContainer"><table border="0" cellpadding="10" cellspacing="0" width="100%"><tr><td class="rightColumnContent"><img src="http://www.hainke.de/_thumbnails_/287_1_Hainke-Filteranlagen-Futterindustrie-135424277.jpg?m=1457700753"  height="200" width="190" class="columnImage" /></td></tr><tr><td valign="top" class="rightColumnContent"><h2>preche mit uns</h2>Lorem ipsum dolor sit amet.</td></tr></table></td></tr></table></td></tr></table></td></tr></table></td></tr></table><table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color:#505050; border:1px solid #353535; border-radius:5px;"><tr><td align="center" valign="middle" style="color:#FFFFFF; font-family:Helvetica, Arial, sans-serif; font-size:16px; font-weight:bold; letter-spacing:-.5px; line-height:150%; padding-top:15px; padding-right:30px; padding-bottom:15px; padding-left:30px;"><a href="http://www.hainke.de" target="_blank" style="color:#FFFFFF; text-decoration:none;">CONTACT HAINKE FILTERANLAGEN GmgH</a></td></tr></table><table border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" id="bodyTable"><tr><td align="center" valign="top"><table border="0" cellpadding="20" cellspacing="0" width="600" id="emailContainer"><tr><td align="center" valign="top" font-size="x-large"><p><strong>An der Imbäke 727798 Hude</strong></p> Postfach 12 4827795 HudeTelefon:    +49 4408 8077-0 Telefax:    +49 4408 8077-10 Internet:     www.hainke.deE-Mail:       info@hainke.de</td></tr></table></td></tr></table>'
    #'<html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /><title></title><style></style></head><body><table border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" id="bodyTable"><tr><td align="center" valign="top"><table border="0" cellpadding="20" cellspacing="0" width="600" id="emailContainer"><tr><td align="center" valign="top">This is where my content goes.</td></tr></table></td></tr></table></body></html><table border="0" cellpadding="0" cellspacing="0" width="600" id="templateColumns"><tr><td align="center" valign="top" width="50%" class="templateColumnContainer"><table border="0" cellpadding="10" cellspacing="0" width="100%"><tr><td class="leftColumnContent"><img src="http://placekitten.com/g/280/300" class="columnImage" /></td></tr><tr><td valign="top" class="leftColumnContent"><h1>Left Column</h1>Lorem ipsum dolor sit amet.</td></tr></table></td><td align="center" valign="top" width="50%" class="templateColumnContainer"><table border="0" cellpadding="10" cellspacing="0" width="100%"><tr><td class="centerColumnContent"><img src="http://placekitten.com/g/280/300" class="columnImage" /></td></tr><tr><td valign="top" class="rightColumnContent"><h1>Right Column</h1>Lorem ipsum dolor sit amet.</td></tr></table></td><td align="center" valign="top" width="50%" class="templateColumnContainer"><table border="0" cellpadding="10" cellspacing="0" width="100%"><tr><td class="rightColumnContent"><img src="http://placekitten.com/g/280/300" class="columnImage" /></td></tr><tr><td valign="top" class="leftColumnContent"><h1>Left Column</h1>Lorem ipsum dolor sit amet.</td></tr></table></td></tr></table>'
    #'<!-- contenido en el centro --><html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /><title></title><style></style></head><body><table border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" id="bodyTable"><tr><td align="center" valign="top"><table border="0" cellpadding="20" cellspacing="0" width="600" id="emailContainer"><tr><td align="center" valign="top">This is where my content goes.</td></tr></table></td></tr></table></body></html><!-- Tabla va aca  --><table border="0" cellpadding="0" cellspacing="0" width="600" id="templateColumns"><tr><td align="center" valign="top" width="50%" class="templateColumnContainer"><table border="0" cellpadding="10" cellspacing="0" width="100%"><tr><td class="leftColumnContent"><img src="http://placekitten.com/g/280/300" class="columnImage" /></td></tr><tr><td valign="top" class="leftColumnContent"><h1>Left Column</h1>Lorem ipsum dolor sit amet.</td></tr></table></td><td align="center" valign="top" width="50%" class="templateColumnContainer"><table border="0" cellpadding="10" cellspacing="0" width="100%"><tr><td class="rightColumnContent"><img src="http://placekitten.com/g/280/300" class="columnImage" /></td></tr><tr><td valign="top" class="rightColumnContent"><h1>Right Column</h1>Lorem ipsum dolor sit amet.</td></tr></table></td></tr></table>'
    #'<html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /><title></title><style></style></head><body><table border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" id="bodyTable"><tr><td align="center" valign="top"><table border="0" cellpadding="20" cellspacing="0" width="600" id="emailContainer"><tr><td align="center" valign="top">This is where my content goes.</td></tr></table></td></tr></table></body></html>' 
    #'<html xmlns="http://www.w3.org/1999/xhtml"> <head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /><title></title><style></style></head><body><table border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" id="bodyTable"><tr><td align="center" valign="top"><table border="0" cellpadding="20" cellspacing="0" width="600" id="emailContainer"><tr><td align="center" valign="top">This is where my content goes.</td></tr></table></td></tr></table></body></html>'
    msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return render(request, 'apli/ingreso.html', {})

#test pdf
class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Proyecto, id=kwargs['pk'])
        #project = get_object_or_404(Proyecto, id=kwargs['pk'])
        template = get_template('invoice.html')
        context = {"project": project,}
        #context = {"client": client,"proyect": proyect,}
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
        if download:
            content = "attachment; filename='{Proyecto.nombre} %s'" %(filename) #poner nombre de proyecto
            response['Content-Disposition'] = content

        return response
        return HttpResponse("Not found")
        
# test pdf

# crear view de proyeto por isma ABIR

class ClienteCreateView(LoginRequiredMixin, CreateView):
    form_class = ClientCreateForm
    login_url = '/login/'
    template_name = 'apli/form.html'
    success_url = "/apli/index_contact"

    def form_valid(self, form):
            instance = form.save(commit=False)
            instance.owner = self.request.user
            return super(ClienteCreateView, self).form_valid(form)

#crar view de proyecto por isma CERRAR


# #register
# class RegisterView(CreateView):
#     form_class = RegisterForm
#     template_name = 'apli/register.html'
#     success_url = "/apli/index_contact"
# #register


@login_required(login_url='/register/login/')
def index_contact(request):
    all_clients = Client.objects.all()
    return render(request, 'apli/index_contact.html', {'all_clients': all_clients})



@login_required(login_url='/register/login/')
def index_model(request):
    all_models = Persona.objects.all()
    return render(request, 'apli/index_model.html', {'all_models': all_models})

@login_required(login_url='/register/login/')
def index_project(request):
    all_projects = Proyecto.objects.all()
    return render(request, 'apli/index_project.html', {'all_projects': all_projects})

@login_required(login_url='/register/login/')
def detail_contact(request, pk):
    client = get_object_or_404(Client, id=pk)
    all_projects = client.proyecto_set.all()
    return render(request, 'apli/detail_contact.html', {'client': client, 'all_projects': all_projects})

@login_required(login_url='/register/login/')
def detail_model(request, persona_id):
    model = get_object_or_404(Persona, id=persona_id)
    return render(request, 'apli/detail_model.html', {'model': model})
    
@login_required(login_url='/register/login/')
def detail_project(request, pk):
    project = get_object_or_404(Proyecto, id=pk)
    return render(request, 'apli/detail_project.html', {'project': project})

@login_required(login_url='/register/login/')
def busca(request):
    query = request.GET.get("q")
    querysetClients = Client.objects.all()
    if query:
        querysetClients = querysetClients.filter(
            Q(nombre_completo__icontains=query)|
            Q(company__icontains=query)|
            Q(email__icontains=query)
        ).distinct()

    querysetPersonas = Persona.objects.all()
    if query:
        querysetPersonas = querysetPersonas.filter(
            Q(nombre_completo__icontains=query)|
            Q(adresse__icontains=query)|
            Q(email__icontains=query)
        ).distinct()

    querysetProyectos = Proyecto.objects.all()
    if query:
        querysetProyectos = querysetProyectos.filter(
            Q(nombre__icontains=query)|
            Q(comment__icontains=query)
        ).distinct()

    return render(request, 'apli/busca.html', {"busca_clients": querysetClients, "busca_personas": querysetPersonas, "busca_proyectos": querysetProyectos})



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
    fields = ['nombre_completo', 'nickname', 'company', 'company_short', 'pais_address', 'ciudad_address', 'codigo_address', 'street_address', 'street_address', 'numero_address', 'email', 'telephone', 'comment']


class ClientUpdate(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ['nombre_completo', 'nickname', 'company', 'company_short', 'pais_address', 'ciudad_address', 'codigo_address', 'street_address', 'street_address', 'numero_address', 'email', 'telephone', 'comment']


class ClientDelete(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('index_contact')



# crear, nueva info y delete proyecto

class ProyectoCreate(LoginRequiredMixin, CreateView):
    model = Proyecto
    fields = ['nombre', 'client', 'comment', 'fecha_creacion', 'fecha_ejecucion']


class ProyectoUpdate(LoginRequiredMixin, UpdateView):
    model = Proyecto
    fields = ['nombre', 'client', 'comment', 'fecha_creacion', 'fecha_ejecucion']


class ProyectoDelete(LoginRequiredMixin, DeleteView):
    model = Proyecto
    success_url = reverse_lazy('index_project')




















