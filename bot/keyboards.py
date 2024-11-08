from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder, InlineKeyboardMarkup
from aiogram import types
from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from text import button_ask_question_text, button_cancel_question_text, button_start_shift_text, button_end_shift_text


send_to_admin_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=button_ask_question_text(), callback_data='ask_question')]
])

cancel_ask_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=button_cancel_question_text(), callback_data='cancel_ask')]
])

start_shift_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=button_start_shift_text(), callback_data='start_shift')]
])

end_shift_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=button_end_shift_text(), callback_data='end_shift')]
])