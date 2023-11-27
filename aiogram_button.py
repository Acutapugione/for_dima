from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

def keyboard_start():

    """ Make start keyboard """

    markup = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text='✅ Так ✅')]],
        resize_keyboard=True
    )

    return markup

def keyboard_approve():

    """Make keyboard approve"""

    inline_btn_1 = InlineKeyboardButton(text='✅ Так, все чудово ✅', callback_data='approve_true')
    inline_btn_2 = InlineKeyboardButton(text='✖️ Вибачте, є помилки ✖️', callback_data='approve_false')
    inline_kb1 = InlineKeyboardMarkup(inline_keyboard=[[inline_btn_1], [inline_btn_2]])

    return inline_kb1