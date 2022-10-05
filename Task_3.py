from email import message
import telebot
from telebot import types

bot = telebot.TeleBot('5527888167:AAFV2XoHi8ELi0sUb0eJbzatH3ZMZgiMscs')
 

del_buttons = telebot.types.ReplyKeyboardRemove()
 
buttons1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons1.row(telebot.types.KeyboardButton('Экспорт формат 1'),
             telebot.types.KeyboardButton('Экспорт формат 2'),
             telebot.types.KeyboardButton('Импорт'))
buttons1.row(telebot.types.KeyboardButton('Выход'))
 
 
@bot.message_handler(commands = ["start", "help"] )
def hello(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Здравствуйте.\nДля работы со справочником выберите пункт из меню.',
                     reply_markup=buttons1)
                   
    bot.register_next_step_handler(msg, answer)
 

@bot.message_handler(content_types=['document']) 
def answer(msg: telebot.types.Message):
    
    if msg.text == 'Экспорт формат 1':
        try:
            bot.register_next_step_handler(msg, export_format1)
            bot.send_message(chat_id=msg.from_user.id,
                        text='Экспортируем файл',
                        reply_markup=del_buttons)
            bot.send_document(chat_id=msg.from_user.id, document=open('my_file.txt', 'rb'))
            bot.send_message(chat_id=msg.from_user.id, text='Файл успешно экспортирован.До свидания!', reply_markup=del_buttons)
        except Exception as e:
            bot.reply_to(message, "Ошибка")  

    elif msg.text == 'Экспорт формат 2':
        try:
            bot.register_next_step_handler(msg, export_format1)
            bot.send_message(chat_id=msg.from_user.id,
                            text='Экспортируем файл',
                            reply_markup=del_buttons)
            bot.send_document(chat_id=msg.from_user.id, document=open('customer_file.txt', 'rb'))
            bot.send_message(chat_id=msg.from_user.id, text='Файл успешно экспортирован. До свидания!', reply_markup=del_buttons)
        except Exception as e:
            bot.reply_to(message, "Ошибка")           
    elif msg.text == 'Импорт':
        try:
            bot.register_next_step_handler(msg, import_file)
            bot.send_message(chat_id=msg.from_user.id,
                     text='Загрузите файл',
                     reply_markup=del_buttons)
            bot.send_document(chat_id=msg.from_user.id, document=open('my_file.txt', 'rb'))
            bot.send_message(chat_id=msg.from_user.id, text='Файл успешно импортирован. До свидания!', reply_markup=del_buttons)
        except Exception as e:
            bot.reply_to(message, "Ошибка")
       
    elif msg.text == 'Выход':

        bot.send_message(chat_id=msg.from_user.id, text='До свидания!', reply_markup=del_buttons)
    else:
        bot.register_next_step_handler(msg, answer)
         

@bot.message_handler(content_types=['document']) 
def export_format1(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=msg.text.upper(), reply_markup=telebot.types.ReplyKeyboardRemove())


@bot.message_handler(content_types=['document'])  
def export_format2(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=msg.text.upper(), reply_markup=telebot.types.ReplyKeyboardRemove())


@bot.message_handler(content_types=['document']) 
def import_file(msg: telebot.types.Message):
    file = bot.get_file(msg.document.file_id)
    downloaded_file = bot.download_file(file.file_path)
    file1 = 'D:\Private\Geekbrains\Python\HW9Pip\customer_file.txt'
    with open(msg.document.file1, 'wb') as new_file:
        new_file.write(downloaded_file)
        bot.reply_to(message, "Пожалуй, я сохраню это")
        bot.send_message(chat_id=msg.from_user.id,
                     text='Данные импортированы',
                     reply_markup=del_buttons)
        bot.register_next_step_handler(msg, answer)
        bot.send_message(chat_id=msg.from_user.id,
                     text='Продолжаем?',
                     reply_markup=buttons1)    

 
bot.polling()
