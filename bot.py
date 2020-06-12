"""
AUTO_BOT bot file

Developers: Andrey Kozlovsky, Stanislav Ermokhin

"""

import datetime
import schedule
import time
import telebot
from telebot import types
from threading import Thread


from config import API_TELEGRAM_TOKEN as TOKEN
import local_en as local
import wrapper_functions
import weather


SECONDS_TO_FETCH = 7
all_seconds = [i for i in range(SECONDS_TO_FETCH)]
TIMES = {(20, 2, all(all_seconds))}

bot = telebot.TeleBot(TOKEN)

user_in_database = wrapper_functions.user_in_database
process_functions_names = ['add_model', 'add_brand', 'add_year',
                           'add_oil', 'add_insurance', 'add_filter',
                           'add_tire', 'add_tech']
info_process_functions_names = ['add_username', 'add_city', 'add_email', 'add_password', 'add_phone']
my_commands = dict(zip(local.buttons_add_keyboard, process_functions_names))
user_info_commands = dict(zip(local.buttons_info_keyboard, info_process_functions_names))


def check_errors(msg, func):
    x = func(msg)

    if x[0]:
        bot.send_message(msg.chat.id, local.success)

    else:
        bot.send_message(msg.chat.id, x[1])


def get_weather_info_on_id(chat_id):
    city = wrapper_functions.get_city_by_chat(chat_id)
    weather_object = weather.CityInfo(city=city)
    dic = weather_object.weather_forecast()
    weather_description = dic['weather'][0]['description']
    if weather_object.description_bad.intersection(weather_description):
        msg_to_send = local.weather_warning + weather_description
        bot.send_message(chat_id=chat_id, text=msg_to_send)

    else:
        pass


def manual_get_weather_info_on_id(chat_id):
    city = wrapper_functions.get_city_by_chat(chat_id)
    weather_object = weather.CityInfo(city=city)
    dic = weather_object.weather_forecast()
    weather_description = dic['weather'][0]['description']
    msg_to_send = local.weather_warning + weather_description
    bot.send_message(chat_id=chat_id, text=msg_to_send)


def send_weather_notification(chat=None):
    if not chat:
        chat_ids = wrapper_functions.get_all_chat_ids()
        for chat_id in chat_ids:
            get_weather_info_on_id(chat_id)

    else:
        manual_get_weather_info_on_id(chat)


@bot.message_handler(commands=['weather'])
def send_on_help(message):
    send_weather_notification(message.chat.id)


@bot.message_handler(commands=['start'])
def send_on_start(message):

    if user_in_database(message.chat.username):
        bot.reply_to(message, local.welcome_back_message1+message.chat.username+local.welcome_back_message2)

    else:
        action = wrapper_functions.add_username(message.chat)
        if action[0]:
            bot.reply_to(message, local.start_response_text + local.success)

        else:
            bot.reply_to(message, local.start_response_text + local.error)


@bot.message_handler(commands=['add'])
def send_on_add(message):

    if user_in_database(message.chat.username):
        markup = types.InlineKeyboardMarkup(row_width=1)

        keyboard_buttons = [types.InlineKeyboardButton(item,
                                                       callback_data=item)
                            for item in local.buttons_add_keyboard]

        for obj in keyboard_buttons:
            markup.add(obj)

        bot.send_message(message.chat.id,
                         local.explain_add_response,
                         reply_markup=markup)

    else:
        bot.reply_to(message, local.error_not_in_database)


@bot.message_handler(commands=['my_info'])
def send_on_info(message):

    if user_in_database(message.chat.username):
        markup = types.InlineKeyboardMarkup(row_width=1)

        keyboard_buttons = [types.InlineKeyboardButton(item,
                                                       callback_data=item)
                            for item in local.buttons_info_keyboard]

        for obj in keyboard_buttons:
            markup.add(obj)

        bot.send_message(message.chat.id,
                         local.explain_info_response,
                         reply_markup=markup)

    else:
        bot.reply_to(message, local.error_not_in_database)


@bot.callback_query_handler(func=lambda call: call.data in my_commands or
                            call.data in user_info_commands or local.okay in call.data)
def get_on_add(call):

    try:
        if call.message:
            if call.data in my_commands:
                msg = bot.reply_to(call.message, text=local.give_value)
                result_function = getattr(wrapper_functions, my_commands[call.data])
                bot.register_next_step_handler(msg, lambda m: check_errors(m, result_function))

            elif call.data in user_info_commands:
                msg = bot.reply_to(call.message, local.give_value)
                result_function = getattr(wrapper_functions, user_info_commands[call.data])
                bot.register_next_step_handler(msg, lambda m: check_errors(m, result_function))

            elif local.okay in call.data:
                data = call.data
                to_find = local.okay + ' '
                key = data[len(to_find):]
                bot.send_message(call.message.chat.id,
                                 text=local.okay_response+': '+key)
                x = wrapper_functions.update_after_notification(call.message, [key])
                if x:
                    bot.send_message(call.message.chat.id,
                                     text=local.success)

                else:
                    bot.send_message(call.message.chat.id, text=local.error)

        else:
            raise Exception('call.message is None/False')  # debugging

    except Exception as e:

        # sending error message to bot for debugging ----------------

        bot.send_message(call.message.chat.id, local.error+'\n'+str(e))
        # -----------------------------------------------------------


def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(1)


def schedule_checker_weather():
    while True:
        schedule.run_pending()
        time.sleep(10)


def send_notification():
    # time check -----
    now_time = datetime.datetime.now().timetuple()
    current_time = (now_time.tm_hour, now_time.tm_min, now_time.tm_sec)

    if current_time in TIMES:  # time check -----
        chat_ids = wrapper_functions.get_all_chat_ids()
        for chat_id in chat_ids:
            dic = wrapper_functions.check_notification(chat_id=chat_id)
            if dic['type'] != ['' for _ in range(len(dic['type']))]:
                markup_okay = types.InlineKeyboardMarkup(row_width=1)
                for item in dic['type']:
                    i = local.types_dict[item]
                    markup_okay.add(types.InlineKeyboardButton(text=local.okay+' '+i,
                                                               callback_data=local.okay+' '+i))
                bot.send_message(chat_id=chat_id,
                                 reply_markup=markup_okay,
                                 text=local.notify_okay)


schedule.every(1).seconds.do(send_notification)  # (every 1 second) or (every 24 hours and clear time check)
t1 = Thread(target=schedule_checker)
t1.setDaemon(True)
t1.start()

schedule.every(10).minutes.do(send_weather_notification)  # weather API limitation
t2 = Thread(target=schedule_checker_weather)
t2.setDaemon(True)
t2.start()

schedule.run_all()


@bot.message_handler(content_types=['text'])
def text_test_run(message):

    # debugging and test --------------------------------------------
    bot.send_message(message.chat.id, 'Reached function text_test_run')
    # ---------------------------------------------------------------


bot.polling()
