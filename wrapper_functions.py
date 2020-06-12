"""
AUTO_BOT db helper file

Developers: Andrey Kozlovsky, Stanislav Ermokhin

"""

import sql
import re
import datetime

import local_ru as local


COLUMNS = {'oil', 'filter', 'insurance', 'tech_check', 'air_tires'}


# Users ----------------------------------------------------------------
def user_city(username):
    """

    :param username: str
    :return: str
    """

    new_conn = sql.DataBase(sql.user, sql.password, sql.host, sql.database)
    city = new_conn.get_user_city(username=username)

    return city


def phone_valid(phone_number):
    """

    :param phone_number:
    :return:
    """

    phone_regex = r'\w{3}-\w{3}-\w{4}'
    if re.search(phone_regex, phone_number):
        return True

    return False


def password_valid(password):
    """

    :param password: str
    :return: bool
    """

    password_length_preference = 8
    caps_regex = r'[A-Z]'
    nums_regex = r'[0-9]'

    if len(password) < password_length_preference:
        return False

    elif not re.search(nums_regex, password):
        return False

    elif not re.search(caps_regex, password):
        return False

    return True


def email_valid(email):
    """

    :param email: str
    :return: bool
    """

    email_regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    if re.search(email_regex, email):
        return True

    return False


def user_in_database(user):
    """

    :param user: str
    :return: bool
    """

    new_conn = sql.DataBase(sql.user, sql.password, sql.host, sql.database)
    query_result = new_conn.select(table='users', columns=['name'])
    query_result_names = [item[0] for item in query_result]

    if user in query_result_names:
        return True

    return False


def add_username(message_chat):
    """

    :param message_chat: dict
    :return: bool or Exception
    """

    try:
        name = message_chat.username
        chat_id = message_chat.id
        new_conn = sql.DataBase(sql.user, sql.password, sql.host, sql.database)
        new_conn.add_user(name=name, chat_id=chat_id)
        user_id = new_conn.get_user_id(username=name)
        new_conn.add_car(user_id=user_id)
        car_id = new_conn.get_car_id(user_id=user_id)
        new_conn.add_now(car_id=car_id)
        new_conn.add_future(car_id=car_id)

        return True, None

    except Exception:
        return False, local.error_cannot_process + '\n' + local.try_again


def add_email(message_chat):
    """

    :param message_chat: dict
    :return: str
    """

    try:
        email = message_chat.text
        if email_valid(email):
            new_conn = sql.DataBase(sql.user, sql.password, sql.host, sql.database)
            user = message_chat.chat.username
            new_conn.update_user_email(username=user, param_value=email)

        else:
            raise Exception(local.email_error)

    except Exception:
        return False, local.email_error + '\n' + local.try_again

    return email, None


def add_phone(message_chat):
    """

    :param message_chat: dict
    :return: str
    """

    try:
        phone_number = message_chat.text
        if phone_valid(phone_number):
            user = message_chat.chat.username
            new_conn = sql.DataBase(sql.user, sql.password, sql.host, sql.database)
            new_conn.update_user_phone(username=user, param_value=phone_number)

        else:
            raise Exception(local.phone_error)

    except Exception:
        return False, local.phone_error + '\n' + local.try_again

    return phone_number, None


def add_password(message_chat):
    """

    :param message_chat: dict
    :return: str
    """

    try:
        password = message_chat.text
        if password_valid(password):
            new_conn = sql.DataBase(sql.user, sql.password, sql.host, sql.database)
            user = message_chat.chat.username
            new_conn.update_user_password(username=user, param_value=password)

        else:
            raise Exception(local.password_error)

    except Exception:
        return False, local.password_error + '\n' + local.try_again

    return password, None


def add_city(message_chat):
    """

    :param message_chat: dict
    :return: str
    """

    try:
        city = message_chat.text
        user = message_chat.chat.username
        new_conn = sql.DataBase(sql.user, sql.password, sql.host, sql.database)
        new_conn.update_user_city(username=user, param_value=city)

    except Exception:
        return False, local.error_cannot_process + '\n' + local.try_again

    return city, None

# ----------------------------------------------------------------------


# Cars -----------------------------------------------------------------
def add_model(message_chat):
    """

    :param message_chat: dict
    :return: bool
    """
    try:
        model = message_chat.text
        user = message_chat.chat.username
        new_conn = sql.DataBase(sql.user, sql.password, sql.host, sql.database)
        user_id = new_conn.get_user_id(user)
        new_conn.update_car_model(user_id, param_value=model)

        return True, None

    except Exception:
        return False, local.error_cannot_process + '\n' + local.try_again


def add_brand(message_chat):
    """

    :param message_chat: dict
    :return: bool
    """
    try:
        brand = message_chat.text
        user = message_chat.chat.username
        new_conn = sql.DataBase(sql.user, sql.password, sql.host, sql.database)
        user_id = new_conn.get_user_id(user)
        new_conn.update_car_brand(user_id, param_value=brand)

        return True, None

    except Exception:
        return False, local.error_cannot_process + '\n' + local.try_again


def add_year(message_chat):
    """

    :param message_chat: dict
    :return: bool
    """
    try:
        year = message_chat.text
        user = message_chat.chat.username
        new_conn = sql.DataBase(sql.user, sql.password, sql.host, sql.database)
        user_id = new_conn.get_user_id(user)
        new_conn.update_car_year(user_id, param_value=year)

        return True, None

    except Exception:
        return False, local.error_cannot_process + '\n' + local.try_again


def add_oil(message_chat):
    """

        :param message_chat: dict
        :return: bool
        """
    try:
        oil = message_chat.text
        user = message_chat.chat.username
        new_conn = sql.DataBase(sql.user, sql.password, sql.host, sql.database)
        user_id = new_conn.get_user_id(user)
        car_id = new_conn.get_car_id(user_id)
        new_conn.oil_update(car_id, oil=oil)

        return True, None

    except Exception:
        return False, local.error_cannot_process + '\n' + local.datetime_format_warning + '\n' + local.try_again


def add_insurance(message_chat):
    """

        :param message_chat: dict
        :return: bool
        """
    try:
        insurance = message_chat.text
        user = message_chat.chat.username
        new_conn = sql.DataBase(sql.user, sql.password, sql.host, sql.database)
        user_id = new_conn.get_user_id(user)
        car_id = new_conn.get_car_id(user_id)
        new_conn.insurance_update(car_id, insurance=insurance)

        return True, None

    except Exception:
        return False, local.error_cannot_process + '\n' + local.datetime_format_warning + '\n' + local.try_again


def add_filter(message_chat):
    """

        :param message_chat: dict
        :return: bool
    """
    try:
        filtr = message_chat.text
        user = message_chat.chat.username
        new_conn = sql.DataBase(sql.user, sql.password, sql.host, sql.database)
        user_id = new_conn.get_user_id(user)
        car_id = new_conn.get_car_id(user_id)
        new_conn.filter_update(car_id, filtr=filtr)

        return True, None

    except Exception:
        return False, local.error_cannot_process + '\n' + local.datetime_format_warning + '\n' + local.try_again


def add_tire(message_chat):
    """

        :param message_chat: dict
        :return: bool
    """
    try:
        tire = message_chat.text
        user = message_chat.chat.username
        new_conn = sql.DataBase(sql.user, sql.password, sql.host, sql.database)
        user_id = new_conn.get_user_id(user)
        car_id = new_conn.get_car_id(user_id)
        new_conn.air_tires_update(car_id, air_tires=tire)

        return True, None

    except Exception:
        return False, local.error_cannot_process + '\n' + local.datetime_format_warning + '\n' + local.try_again


def add_tech(message_chat):
    """

        :param message_chat: dict
        :return: bool
    """
    try:
        tech = message_chat.text
        user = message_chat.chat.username
        new_conn = sql.DataBase(sql.user, sql.password, sql.host, sql.database)
        user_id = new_conn.get_user_id(user)
        car_id = new_conn.get_car_id(user_id)
        new_conn.tech_check_update(car_id, tech_check=tech)

        return True, None

    except Exception:
        return False, local.error_cannot_process + '\n' + local.datetime_format_warning + '\n' + local.try_again
# ----------------------------------------------------------------------


def get_city_by_chat(chat):
    try:
        new_conn = sql.DataBase(sql.user, sql.password, sql.host, sql.database)
        return new_conn.get_user_city_by_chat(chat)

    except Exception:
        return False


def get_all_chat_ids():
    try:
        new_conn = sql.DataBase(sql.user, sql.password, sql.host, sql.database)
        return new_conn.get_chat_ids()

    except Exception:
        return []


def do_text(notification_type_item):
    """

    :param notification_type_item: str
    :return: str
    """

    columns = COLUMNS

    if notification_type_item in columns:
        if notification_type_item == 'filter':
            return getattr(local, '_' + notification_type_item)
        else:
            return getattr(local, notification_type_item)

    else:
        return ''


def check_notification(chat_id):
    """

    :param chat_id: telegram chat id
    :return: dict or Exception
    """
    try:
        new_conn = sql.DataBase(sql.user, sql.password, sql.host, sql.database)
        user_id = new_conn.get_user_id_by_chat(chat_id=chat_id)
        car_id = new_conn.get_car_id(user_id=user_id)
        dates_dict = new_conn.get_car_notification(car_id)
        current_date = datetime.datetime.now().date()
        # to notify the same day
        if current_date in [value
                            for value in dates_dict.values()]:
            return {'date': current_date,
                    'chat_id': chat_id,
                    'type': [key
                             for key in dates_dict
                             if dates_dict[key] == current_date]}

        else:
            return dict()

    except Exception:
        return False


def update_after_notification(message, keys):
    """

    :param message: str
    :param keys: list
    :return: bool or Exception
    """

    try:
        chat_id = message.chat.id
        for key in keys:
            new_conn = sql.DataBase(sql.user, sql.password, sql.host, sql.database)
            user_id = new_conn.get_user_id_by_chat(chat_id=chat_id)
            car_id = new_conn.get_car_id(user_id=user_id)
            today = datetime.datetime.now()
            getattr(new_conn, key+'_update')(car_id, today.strftime('%Y-%m-%d %H:%M:%S'))

        return True

    except Exception:
        return False
