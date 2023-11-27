from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from settings import APPROVE_MENU

    
def keyboard_start():
    """Make start keyboard"""
    reply_builder = ReplyKeyboardBuilder()
    reply_builder.button(text='✅ Так ✅')
    return reply_builder.as_markup()

def keyboard_approve():
    """Make keyboard approve"""
    inline_builder = InlineKeyboardBuilder()
    
    for key, val in APPROVE_MENU.items():
        inline_builder.button(text=val, callback_data=key)
    inline_builder.adjust(1, 1)    
    return inline_builder.as_markup()