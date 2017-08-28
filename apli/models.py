from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.CharField(max_length=200)
    name_short = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=200, blank=True)
    company_short = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=15)
    comment = models.CharField(max_length=500, blank=True)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def get_absolute_url(self):
        return reverse('detail_client', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    start = models.DateField()
    finish = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, blank=True)
    sort = models.CharField(max_length=8, choices=(('Angebot', 'angebot'), ('Auftrag', 'aufttrag'), ('Job', 'job'),), default='Angebot')
    statut = models.CharField(max_length=9, choices=(('Project', 'project'), ('Bestätigung', 'confirmed'), ('Fertig', 'realized'), ('bezhal', 'acquitted'), ('Absagen', 'canceled'),), default='Project')
    all_day = models.IntegerField(null=True, blank=True)
    half_day = models.IntegerField(null=True, blank=True)
    half_day_price_pro = models.IntegerField(null=True, blank=True)
    all_day_price_pro = models.IntegerField(null=True, blank=True)
    over_price_pro = models.IntegerField(null=True, blank=True)
    all_in_price_pro = models.IntegerField(null=True, blank=True)
    half_day_price_semipro = models.IntegerField(null=True, blank=True)
    all_day_price_semipro = models.IntegerField(null=True, blank=True)
    over_price_semipro = models.IntegerField(null=True, blank=True)
    all_in_price_semipro = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=100, blank=True)
    comment_address = models.CharField(max_length=500, blank=True)
    honorary_base = models.IntegerField(null=True, blank=True)
    honorary_plus = models.IntegerField(null=True, blank=True)
    quantity_models_honorary_plus = models.IntegerField(null=True, blank=True)
    ms_price = models.IntegerField(null=True, blank=True)
    ms_hours = models.IntegerField(null=True, blank=True)
    requirement_price = models.IntegerField(null=True, blank=True)
    requirement_hours = models.IntegerField(null=True, blank=True)
    requisiten_price_for_each_model = models.IntegerField(null=True, blank=True)
    other_title = models.CharField(max_length=50, blank=True)
    other_description = models.CharField(max_length=200, blank=True)
    other_price = models.IntegerField(null=True, blank=True)
    other_hours = models.IntegerField(null=True, blank=True)
    photo_price = models.IntegerField(null=True, blank=True)
    photo_hours = models.IntegerField(null=True, blank=True)
    total_price = models.IntegerField(null=True, blank=True)
    tax = models.IntegerField(default=19)

    def get_absolute_url(self):
        return reverse('detail_project', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=200)
    name_short = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=200, blank=True)
    company_short = models.CharField(max_length=100, blank=True)
    agent = models.CharField(max_length=200, blank=True)
    agent_short = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=15)
    comment = models.CharField(max_length=500, blank=True)
    sedcard = models.BooleanField(default=False)
    statut = models.CharField(max_length=15, choices=(('modell', 'Modelo'), ('Photograph', 'Fotografo'), ('Make Up', 'Make Up'), ('Styling', 'Styling'), ('Rrhh', 'Recursos Humanos'), ('verschieden', 'Otro')), default='Modell')
    bank_regex = RegexValidator(regex=r'^DE\d{2}\s?([0-9a-zA-Z]{4}\s?){4}[0-9a-zA-Z]{2}$', message="Bank account must be entered in the format: 'DE12 3456 7890 1234 5678 90'. Up to 27 digits allowed.")
    bank_account = models.CharField(validators=[bank_regex], max_length=27)
    website = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

    def get_absolute_url(self):
        return reverse('detail_model', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Attachment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    sort = models.CharField(max_length=8)
    file = models.FileField()
    send_date = models.DateField()
    answer_date = models.DateField(null=True, blank=True)
    statut = models.CharField(max_length=14, choices=(('waiting answer', 'waiting answer'), ('accepted', 'accepted'), ('rejected', 'rejected'),), default='waiting answer')
    comment_WG = models.CharField(max_length=500, blank=True)
    comment_client = models.CharField(max_length=500, blank=True)

    class Meta:
        verbose_name = 'Attachment'
        verbose_name_plural = 'Attachments'

    def __str__(self):
        return self.sort



class Assignment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    model_type = models.CharField(max_length=14, choices=(('pro', 'pro'), ('semipro', 'semipro'),), default='pro')
    travel_cost = models.IntegerField(null=True, blank=True)
    hotel_cost = models.IntegerField(null=True, blank=True)
    other_cost = models.IntegerField(null=True, blank=True)
    comment_WG = models.CharField(max_length=500, blank=True)
    comment_model = models.CharField(max_length=500, blank=True)
    statut = models.CharField(max_length=14, choices=(('created', 'created'), ('waiting answer', 'waiting answer'), ('confirmed', 'confirmed'), ('not possible', 'not possible'), ('realized', 'realized'), ('acquitted', 'acquitted'),), default='created')
    send_date = models.DateField(null=True, blank=True)
    confirmation_date = models.DateField(null=True, blank=True)
    payment_date = models.DateField(null=True, blank=True)
    total_price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.person.name + ' - ' + self.project.name


class Horaire(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    finish_time = models.TimeField()


class Cost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, blank=True)
    date = models.DateField()
    amount = models.IntegerField()
    title = models.CharField(max_length=100)
    statut = models.CharField(max_length=14, choices=(('planned', 'planned'), ('complete', 'complete'),), default='planned')
