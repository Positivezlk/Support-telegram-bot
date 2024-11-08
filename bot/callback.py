from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from bot_instance import bot
from keyboards import cancel_ask_keyboard, send_to_admin_keyboard, end_shift_keyboard, start_shift_keyboard
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.context import FSMContext
from states import Form
from text import create_question_text, cancel_create_question_text, admin_panel_text, button_end_shift_text, end_shift_text
from config import IsUserContactedSupport
from states import Form, Form2
from db.sql_command import set_shift_admin, check_shift_admin
from handlers import delete_one_msg
import asyncio

router = Router()


@router.callback_query(F.data == 'ask_question')
async def create_question(callback: CallbackQuery, state: FSMContext):
    IsUserContactedSupport.VALUE = True
    await state.set_state(Form.create_question)
    await state.update_data(panel_id=callback.message.message_id)
    await bot.edit_message_text(chat_id=callback.message.chat.id, 
                                message_id=callback.message.message_id, 
                                text=create_question_text(), 
                                reply_markup=cancel_ask_keyboard, 
                                parse_mode=ParseMode.HTML)
    

@router.callback_query(F.data == 'cancel_ask')
async def cancel_create_question(callback: CallbackQuery, state: FSMContext):
    IsUserContactedSupport.VALUE = False
    await state.clear()
    await bot.edit_message_text(chat_id=callback.message.chat.id, 
                                message_id=callback.message.message_id, 
                                text=cancel_create_question_text(), 
                                reply_markup=send_to_admin_keyboard, 
                                parse_mode=ParseMode.HTML)
    

@router.callback_query(F.data == 'start_shift')
async def start_shift(callback: CallbackQuery, state: FSMContext):
    if await check_shift_admin(callback.message.chat.id) == 0:
        await set_shift_admin(callback.message.chat.id, 1)
        await bot.edit_message_text(chat_id=callback.message.chat.id,
                                    message_id=callback.message.message_id,
                                    text=admin_panel_text(),
                                    reply_markup=end_shift_keyboard,
                                    parse_mode=ParseMode.HTML)
    else:
        msg_id = (await bot.edit_message_text(chat_id=callback.message.chat.id,
                                    message_id=callback.message.message_id,
                                    text='Вы уже и так на смене!',
                                    parse_mode=ParseMode.HTML)).message_id
        await asyncio.sleep(5)
        await delete_one_msg(callback.message, msg_id)
    
@router.callback_query(F.data == 'end_shift')
async def end_shift(callback: CallbackQuery, state: FSMContext):
    if await check_shift_admin(callback.message.chat.id) == 1:
        await set_shift_admin(callback.message.chat.id, 0)
        await bot.edit_message_text(chat_id=callback.message.chat.id,
                                    message_id=callback.message.message_id,
                                    text=end_shift_text(),
                                    reply_markup=start_shift_keyboard,
                                    parse_mode=ParseMode.HTML)
    else:
        msg_id = (await bot.edit_message_text(chat_id=callback.message.chat.id,
                                    message_id=callback.message.message_id,
                                    text='Вы и так не на смене!',
                                    parse_mode=ParseMode.HTML)).message_id
        await asyncio.sleep(5)
        await delete_one_msg(callback.message, msg_id)


@router.callback_query(F.data == 'answer_user')
async def answer_user(callabck: CallbackQuery, state: FSMContext):
    await state.set_state(Form2.send_answer)
    await callabck.message.answer('Напишите ID пользователя и ответ на вопрос через "/"')
