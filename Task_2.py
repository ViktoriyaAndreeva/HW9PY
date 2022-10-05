#Калькулятор

from email import message
import telebot
from telebot import types

bot = telebot.TeleBot('5527888167:AAFV2XoHi8ELi0sUb0eJbzatH3ZMZgiMscs')

user_num1 = ""
user_num2 = ""
user_operation = ""
user_result = None


@bot.message_handler(commands = ["start", "help"] )
def send_first_message(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    msg = bot.send_message(message.chat.id, "Привет! я бот-калькулятор\nВведите первое число", reply_markup=markup)
    bot.register_next_step_handler(msg, process_num1_step)


def process_num1_step(message, user_result = None):
    try:
        global user_num1
        if user_result == None:
                user_num1 = int(message.text)
        else:
            user_num1 = str(user_result)
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        itembutton1 = types.KeyboardButton('+')
        itembutton2 = types.KeyboardButton('-')
        itembutton3 = types.KeyboardButton('*')
        itembutton4 = types.KeyboardButton('/')
        markup.add(itembutton1, itembutton2, itembutton3, itembutton4)

        msg = bot.send_message(message.chat.id, "Выберите операцию", reply_markup=markup)
        bot.register_next_step_handler(msg, process_operation_step)
    except Exception as e:
        bot.reply_to(message, "Введите число!")


def process_operation_step(message):
    try:
        global user_operation
        user_operation = message.text
        markup = types.ReplyKeyboardRemove(selective=False)
        msg = bot.send_message(message.chat.id, "Введите еще число", reply_markup=markup)
        bot.register_next_step_handler(msg, process_num2_step)
    except Exception as e:
            bot.reply_to(message, "Введите число!")


def process_num2_step(message):
    try:
        global user_num2
        user_num2 = int(message.text)
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        itembutton1 = types.KeyboardButton('результат')
        itembutton2 = types.KeyboardButton('считаем дальше')
        markup.add(itembutton1, itembutton2)

        msg = bot.send_message(message.chat.id, "Смотрим результат или продолжаем вычислять?", reply_markup=markup)
        bot.register_next_step_handler(msg, process_alternative_step)
    except Exception as e:
            bot.reply_to(message, "Введите число!")


def process_alternative_step(message):
    try:
        calc()
        
        markup = types.ReplyKeyboardRemove(selective=False)
        
        if message.text.lower() == "результат":
            bot.send_message(message.chat.id, print_calculator(), reply_markup=markup)
        elif message.text.lower() == "считаем дальше":
            process_num1_step(message, user_result)
    except Exception as e:
            bot.reply_to(message, "Ошибка!")


def print_calculator():
    global user_num1, user_num2, user_operation, user_result
    return "Результат: " + str(user_num1) + ' ' + user_operation + ' ' + str(user_num2) + ' = ' + str(user_result)


def calc():
    global user_num1, user_num2, user_operation, user_result
    user_result = eval(str(user_num1) + user_operation + str(user_num2))
    return user_result


bot.polling(none_stop=True, interval=0)
