from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    create_question = State()

class Form2(StatesGroup):
    send_answer = State()
