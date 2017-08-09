from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_even(value):
	if value % 2 != 0:
		raise ValidationError(
		'%(value)s is not an even number',
		params={'value': value},
		)
		
def clean_email(value):
		email = value
		if ".edu" in email:
			raise ValidationError("We do not accept edu emails")