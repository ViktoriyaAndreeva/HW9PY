import telebot
 
bot = telebot.TeleBot('5527888167:AAFV2XoHi8ELi0sUb0eJbzatH3ZMZgiMscs')
 

del_buttons = telebot.types.ReplyKeyboardRemove()
 
buttons1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons1.row(telebot.types.KeyboardButton('Комплексные'),
             telebot.types.KeyboardButton('Рациональные'),
             telebot.types.KeyboardButton('Комплексные1'),
             telebot.types.KeyboardButton('Рациональные2'))
buttons1.row(telebot.types.KeyboardButton('Ещё не определился'))
 
buttons2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons2.row(telebot.types.KeyboardButton('+'),
             telebot.types.KeyboardButton('-'))
buttons2.row(telebot.types.KeyboardButton('*'),
             telebot.types.KeyboardButton('/'))
 
 
@bot.message_handler(commands=['log'])
def hello(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Лог программы\newcoiywgecowegcouwefoyewfov',
                     reply_markup=del_buttons)
 
 
@bot.message_handler()
def hello(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Здравствуйте.\nВыберите режим работы калькулятора.',
                     reply_markup=buttons1)
    bot.register_next_step_handler(msg, answer)
 
 
def answer(msg: telebot.types.Message):
    if msg.text == 'Комплексные':
        bot.register_next_step_handler(msg, complex_counter)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Введите выражение с комплексными числами.',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    elif msg.text == 'Рациональные':
        bot.register_next_step_handler(msg, first_step_rational)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Введите число.',
                         reply_markup=del_buttons)
    elif msg.text == 'Ещё не определился':
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id, text='Возвращайтесь, когда определитесь.')
    else:
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id, text='Пожалуйста, используйте кнопки.')
 
        bot.send_message(chat_id=msg.from_user.id, text='Выберите режим работы калькулятора.', reply_markup=buttons1)
 

def first_step_rational(msg: telebot.types.Message):
   
    if msg.text.isdigit():
        bot.register_next_step_handler(msg, second_step_rational)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Введите второе число.',
                         reply_markup=del_buttons)
    else:
        bot.register_next_step_handler(msg, first_step_rational)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Введите правильно первое число!',
                         reply_markup=del_buttons)


def second_step_rational(msg: telebot.types.Message):
    if msg.text.isdigit():
        bot.register_next_step_handler(msg, third_step_rational)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Введите выражение.',
                         reply_markup=buttons2)
    else:
        bot.register_next_step_handler(msg, second_step_rational)
        bot.send_message(chat_id=msg.from_user.id,
                         text='Введите правильно второе число!',
                         reply_markup=del_buttons)
                    
def third_step_rational(msg: telebot.types.Message):
    if msg.text in {"+", "-", "*", "/"}:
        if msg.text == "+":
            pass
    else:
        bot.send_message(chat_id=msg.from_user.id,
                         text='Используйте кнопки!',
                         reply_markup=buttons2)



def complex_counter(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=msg.text.upper(), reply_markup=telebot.types.ReplyKeyboardRemove())
 
 
def rational_counter(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=msg.text.lower(), reply_markup=telebot.types.ReplyKeyboardRemove())
 
 
bot.polling()