from django.shortcuts import render
from django.http import HttpResponse
from fullcalendar.models import CalendarEvent
from fullcalendar.util import events_to_json, calendar_options
from fullcalendar.forms import NewTask
from django.contrib.auth.decorators import login_required # requisito login  def
from django.contrib.auth.mixins import LoginRequiredMixin # requisito login  viw
from django.views.generic.edit import CreateView, UpdateView, DeleteView


@login_required(login_url='/register/login/')
def index_task(request):
    all_tasks = CalendarEvent.objects.all()
    return render(request, 'task/index_task.html', {'all_tasks': all_tasks})

@login_required(login_url='/register/login/')
def detail_task(request, pk):
    task = get_object_or_404(CalendarEvent, id=pk)
    return render(request, 'task/detail_task.html', {'task': task})

    # crear una nuev task
class new_task(LoginRequiredMixin, CreateView):
    form_class = NewTask
    login_url = '/login/'
    template_name = 'task/form_task.html'
    success_url = "/calendar/task"

    def form_valid(self, form):
            instance = form.save(commit=False)
            instance.owner = self.request.user
            return super(new_task, self).form_valid(form)


OPTIONS = """{  header: {
                    left: 'prev,next today',
                    center: 'title',
                    right: 'month,agendaWeek,agendaDay,listYear',
                },
                allDaySlot: false,
                firstDay: 1, //empezando la semana por lunes
                slotDuration: '00:30:00',
                minTime: "08:00:00", // hora de entrada
                maxTime: "20:00:00", // y salida kaka
                editable: true,
                //weekNumbers: true,
                height: 550,

                timeFormat: 'HH:mm',
                columnFormat: 'ddd D/M',

                listDayFormat: 'dddd D MMMM YYYY',

                views: {
                    basic: {
                    },
                    agenda: {
                        titleFormat: 'DD MMMM YYYY',
                    },
                    week: {
                        titleFormat: 'DD MMMM YYYY',
                    },
                    day: {
                        titleFormat: 'D MMMM YYYY',
                    }
                },

                monthNames: ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio',
                    'Agosto','Septiembre','Octubre','Noviembre','Diciembre'],
                monthNamesShort:
                    ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic'],
                dayNames: ['Domingo','Lunes','Martes','Miercoles','Jueves','Viernes','Sabado'],
                dayNamesShort: ['Dom', 'Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab'],
                buttonText : {
                    prev:     '<<',  // left triangle
                    next:     '>>',  // right triangle
                    prevYear: '&nbsp;&lt;&lt;&nbsp;', // <<
                    nextYear: '&nbsp;&gt;&gt;&nbsp;', // >>
                    today:    'Hoy',
                    month:    'Mes',
                    week:     'Semana',
                    day:      'Dia'
                },

                dayClick: function(date, jsEvent, view) {
                    alert('Clicked on: ' + date.format());
                    alert('Coordinates: ' + jsEvent.pageX + ',' + jsEvent.pageY);
                    alert('Current view: ' + view.name);
                    $('#calendar').fullCalendar('gotoDate', date)
//                    $(this).css('background-color', 'red');
//                    $('#calendar').fullCalendar('changeView', 'agendaDay')
                },

                eventClick: function(event) {
                    window.open(event.url, "_self");
                    return false;
                }


            }"""


def index(request):
    event_url = 'all_events/'
    return render(request, 'fullcalendar/index.html', {'calendar_config_options': calendar_options(event_url, OPTIONS)})


def all_events(request):
    current_user = request.user.id
    events = CalendarEvent.objects.filter(responsable=current_user)
    return HttpResponse(events_to_json(events), content_type='application/json')
