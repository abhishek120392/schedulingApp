from datetime import datetime

def datetime_in_ist(unaware_datetime=None):
	if unaware_datetime is None:
	    unaware_datetime = datetime.now()
	if unaware_datetime.tzinfo is None:
	    utc_curr_time = UTC.localize(unaware_datetime)
	else:
	    utc_curr_time = unaware_datetime
	ist = timezone('Asia/Kolkata')
	ist_curr_time = utc_curr_time.astimezone(ist)
	return ist_curr_time

def validateEmail(email):
  from django.core.validators import validate_email
  from django.core.exceptions import ValidationError
  try:
      validate_email( email )
      return True
  except ValidationError:
      return False	