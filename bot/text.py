from aiogram.types import Message
from db.sql_command import output_name_admin

def  hello_user_text(message: Message):
    return f'👋<b>Здравствуйте</b>, <b>{message.from_user.first_name}</b>, я бот службы поддержки, помогу вам быстро решить проблему!\n\nЕсли хотите задать вопрос, нажмите на <b>кнопку</b> ниже👇'

def create_question_text():
    return '<b>Расскажите о своей проблеме, а я обязательно помогу!</b> ✍\n\nЕсли передумали, нажмите на кнопку ниже 👇'

def cancel_create_question_text():
    return '🟢 Если вдруг возникнут вопросы, <b><u>обязательно обращайтесь!</u></b>'

def mail_sent_successfully_text():
    return '📩 <b>Сообщение уже отправлено в службу поддержки!</b>\nВ течении <u>5 минут</u> вам <b>ответят!</b>\n\nЕсли хотите что то добавить, нажмите на <b>кнопку</b> ниже 👇'

def forbidden_access_text():
    return '🚫 Извините, но у вас нету доступа к этой команде. 🚫'

async def hello_admin_text(message: Message):
    name = await output_name_admin(message.chat.id)
    return f'👋 Здравствуйте, <b>{name}!</b>\nЖелаете начать смену?'

def admin_panel_text():
    return '<b>Вы начали смену, приятной работы!</b>🧑‍💻'

def end_shift_text():
    return '<b>Вы закончили смену, всего доброго!</b> 👋'

def already_on_shift():
    return '<b>Вы и так уже на смене!</b>'

def already_finish_shitf():
    return '<b>Вы и так не на смене!<b>'

def message_from_admin(answer):
    return f'СООБЩЕНИЕ ОТ СЛУЖБЫ ПОДДЕРЖКИ:\n\n{answer}'

def message_sent_text():
    return 'сообщение отправлено'

def error_sent_msg_text():
    return 'ОШИБКА, попробуйте еще раз'


def emoji_mail():
    return '📨'


def button_ask_question_text():
    return '❗ Задать вопрос ❗'

def button_cancel_question_text():
    return '❌ Отмена ❌'

def button_start_shift_text():
    return '💼 Начать смену 💼'

def button_end_shift_text():
    return '🏁 Закончить смену 🏁'

def button_read_question_text():
    return 'Прочитать'

def button_get_msg_from_user(message: Message):
    return f'<b>СООБЩЕНИЕ ОТ ПОЛЬЗОВАТЕЛЯ</b> {message.chat.id}'

def button_answer_user_text(message: Message):
    return 'Ответить пользователю'
