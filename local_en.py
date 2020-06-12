"""
AUTO_BOT localization file

Developers: Andrey Kozlovsky, Stanislav Ermokhin

"""

from datetime import datetime

help_response_text = datetime.now()
start_response_text = 'You seem to be new around here\nUser added status: '
welcome_back_message1 = 'Welcome back, '
welcome_back_message2 = '!'
explain_add_response = 'We will now collect info about your vehicle'
error_not_in_database = 'Error! You haven\'t registered yet!'
error_cannot_process = 'I can\'t process this command'
give_value = 'Type value'
success = 'Success!'
error = 'Error!'
notify_okay = 'There\'s data to update'
okay = 'Okay, now update my data: '
okay_response = 'Updating data...'

buttons_add_keyboard = ['Car model', 'Car brand', 'Year of production', 'Prev. oil change date',
                        'Prev. insurance change date', 'Prev. oil filter change date',
                        'Prev. tire inflation date', 'Prev. tech check date']
datetime_format_warning = 'Dates should be YYYY-MM-DD HH:MM:SS'
buttons_info_keyboard = ['Username', 'City', 'E-mail', 'Password', 'Phone']
explain_info_response = 'We will now collect your info'
password_error = 'Password must contain numbers and capital letters, and be of length >= 8'
email_error = 'Incorrect e-mail address'
phone_error = 'Phone number should be XXX-XXX-XXXX (no country code)'

try_again = 'Try doing it again'

oil = 'oil'
_filter = 'filter'
insurance = 'insurance'
tech_check = 'tech_check'
air_tires = 'air_tires'

types_dict = {oil: oil,
              _filter: _filter,
              insurance: insurance,
              tech_check: tech_check,
              air_tires: air_tires}

weather_warning = 'Be careful!\nWeather in your city now:\n'
