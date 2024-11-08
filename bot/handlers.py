from bot_instance import dp, bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from text import hello_user_text, mail_sent_successfully_text, emoji_mail, forbidden_access_text, hello_admin_text, admin_panel_text, end_shift_text, already_on_shift, already_finish_shitf, button_read_question_text, button_get_msg_from_user, button_answer_user_text, message_from_admin, message_sent_text, error_sent_msg_text
from aiogram.enums.parse_mode import ParseMode
from keyboards import send_to_admin_keyboard, start_shift_keyboard, end_shift_keyboard
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder, InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from states import Form, Form2
import asyncio
from config import IsUserContactedSupport
from db.sql_command import add_new_user_question, output_list_admin, set_shift_admin, check_shift_admin, output_all_id_questions, add_to_existing_question, output_admins_on_shift, output_user_question
from random import randint

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    if message.chat.id in await output_list_admin():
        greeting = await hello_admin_text(message)
        await message.answer(text=greeting, 
                             reply_markup=start_shift_keyboard,
                             parse_mode=ParseMode.HTML)
    else:
        await message.answer(text=hello_user_text(message), reply_markup=send_to_admin_keyboard, parse_mode=ParseMode.HTML)


@router.message(Command('admin'))
async def admin_panel(message: Message):
    if message.chat.id in await output_list_admin():
        greeting = await hello_admin_text(message)
        await message.answer(text=greeting, 
                             reply_markup=start_shift_keyboard,
                             parse_mode=ParseMode.HTML)
    else:
        msg_id = (await message.answer(text=forbidden_access_text())).message_id
        await asyncio.sleep(5)
        await delete_some_msg(message, msg_id)


@router.message(Command('startshift'))
async def start_shift(message: Message):
    if message.chat.id in await output_list_admin():
        if await check_shift_admin(message.chat.id) == 0:
            await set_shift_admin(message.chat.id, 1)
            await message.answer(text=admin_panel_text(),
                                reply_markup=end_shift_keyboard,
                                parse_mode=ParseMode.HTML)
        else:
            msg_id = (await message.answer(text=already_on_shift(),
                                 parse_mode=ParseMode.HTML)).message_id
            await asyncio.sleep(5)
            await delete_some_msg(message, msg_id)
    else:
        msg_id = (await message.answer(text=forbidden_access_text())).message_id
        await asyncio.sleep(5)
        await delete_some_msg(message, msg_id)


@router.message(Command('endshift'))
async def end_shift(message: Message):
    if message.chat.id in await output_list_admin():
        if await check_shift_admin(message.chat.id) == 1:
            await set_shift_admin(message.chat.id, 0)
            await message.answer(text=end_shift_text(),
                                 reply_markup=start_shift_keyboard,
                                 parse_mode=ParseMode.HTML)
        else:
            msg_id = (await message.answer(text=already_finish_shitf(),
                                 parse_mode=ParseMode.HTML)).message_id
            await asyncio.sleep(5)
            await delete_some_msg(message, msg_id)
    else:
        msg_id = (await message.answer(text=forbidden_access_text())).message_id
        await asyncio.sleep(5)
        await delete_some_msg(message, msg_id)

user = 0
@router.message(Form.create_question)
async def get_user_question_1(message: Message, state: FSMContext):
    global user
    data = await state.get_data()
    panel_id = data['panel_id']
    user = message.chat.id
    if message.chat.id not in await output_all_id_questions():
        check_question_keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=button_read_question_text(), callback_data='check_text')]
        ], )
        await add_new_user_question(user_id=message.chat.id, question=message.text)
        admins_on_shift =  await output_admins_on_shift()
        selected_admin = admins_on_shift[randint(0, len(admins_on_shift) - 1)]
        await bot.send_message(chat_id=selected_admin, 
                               text=button_get_msg_from_user(message),
                                reply_markup=check_question_keyboard,
                               parse_mode=ParseMode.HTML)
    else:
        await add_to_existing_question(user_id=message.chat.id, question=message.text)
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await bot.delete_message(chat_id=message.chat.id, message_id=panel_id)
    msg = await message.answer(text=emoji_mail())
    await asyncio.sleep(2)
    await get_user_question_2(message, panel_id, msg.message_id, state)
    IsUserContactedSupport.VALUE = False

@router.callback_query(F.data == 'check_text')
async def check_text(callback: CallbackQuery):
    user_id = user
    print(user_id)
    text = await output_user_question(user_id=user_id)
    answer_user = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=button_answer_user_text(), callback_data='answer_user')]
    ], )
    await callback.message.answer(f'<code>{text}</code>', parse_mode='HTML', reply_markup=answer_user)


async def get_user_question_2(message: Message, panel_id, msg_id, state: FSMContext):
    await bot.delete_message(chat_id=message.chat.id, message_id=msg_id)
    await state.clear()
    await message.answer(text=mail_sent_successfully_text(), 
                         reply_markup=send_to_admin_keyboard, 
                         parse_mode=ParseMode.HTML)
    

@router.message(Form2.send_answer)
async def answer_user(message: Message, state: FSMContext):
    try:
        id, answer = message.text.split('/')
        await bot.send_message(chat_id=id, text=message_from_admin(answer))
        await message.answer(text=message_sent_text())
    except Exception:
        await message.answer(text=error_sent_msg_text())


@router.message()
async def check_new_msg(message: Message):
    if IsUserContactedSupport.VALUE == False and message.chat.id not in await output_list_admin():
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


async def delete_some_msg(message: Message, msg_id):
    await bot.delete_message(chat_id=message.chat.id, message_id=msg_id)
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


async def delete_one_msg(message: Message, msg_id):
    await bot.delete_message(chat_id=message.chat.id, message_id=msg_id)