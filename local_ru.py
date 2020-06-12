"""
AUTO_BOT localization file

Developers: Andrey Kozlovsky, Stanislav Ermokhin

"""

from datetime import datetime

help_response_text = datetime.now()
start_response_text = 'Вы здесь впервые\nСтатус добавления пользователя: '
welcome_back_message1 = 'Мы рады, что Вы вернулись, '
welcome_back_message2 = '!'
explain_add_response = 'Сейчас мы соберём информацию о Вашем транспорте'
error_not_in_database = 'Ошибка! Вы ещё не зарегистрировались!'
error_cannot_process = 'Невозможно обработать команду'
give_value = 'Укажите значение'
success = 'Успех!'
error = 'Ошибка!'
notify_okay = 'Надо обновить данные'
okay = 'Окей, обновите данные о: '
okay_response = 'Обновляем данные...'

buttons_add_keyboard = ['Модель автомобиля', 'Брэнд автомобиля', 'Год производства', 'Пред. замена масла',
                        'Пред. обновление страховки', 'Пред. замена фильтра',
                        'Пред. подкачка шин', 'Пред. ТО']
datetime_format_warning = 'Дата должна удовлетворять формату YYYY-MM-DD HH:MM:SS'
buttons_info_keyboard = ['Имя пользователя', 'Город', 'E-mail', 'Пароль', 'Телефон']
explain_info_response = 'Сейчас мы соберём информацию о Вас'
password_error = 'Пароль должен содержать цифры, заглавные буквы и быть длинною >= 8'
email_error = 'Неправильный e-mail адрес'
phone_error = 'Номер телефона должен удовлетворять формату XXX-XXX-XXXX (без +7)'

try_again = 'Попробуйте снова. Не забудьте нажать на кнопку.'

oil = 'oil'
_filter = 'filter'
insurance = 'insurance'
tech_check = 'tech_check'
air_tires = 'air_tires'

types_dict = {oil: 'Замена масла',
              _filter: 'Замена фильтра',
              insurance: 'Обновление страховки',
              tech_check: 'ТО',
              air_tires: 'Подкачка шин'}

weather_warning = 'Будьте осторожны!\nПогода в Вашем городе сейчас:\n'
