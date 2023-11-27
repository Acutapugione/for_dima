import asyncio
import logging
import sys
from dotenv import load_dotenv
from os import getenv
from typing import Any, Dict

from aiogram import Bot, Dispatcher, F, Router, html
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    CallbackQuery,
)
from diff import check_pdf
from aiogram_button import keyboard_approve


load_dotenv()
GROUP_ID = getenv("GROUP_ID")
TELE_BOT_API_KEY = getenv("TELE_BOT_API_KEY")
bot = Bot(token=TELE_BOT_API_KEY, parse_mode=ParseMode.HTML)

form_router = Router()


class Form(StatesGroup):
    contact = State()
    document = State()


@form_router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.contact)
    await message.answer(
        "Ваш контакт",
        reply_markup=ReplyKeyboardRemove(),
    )

@form_router.message(Form.contact)
async def process_name(message: Message, state: FSMContext) -> None:
    if message.document:
        await state.update_data(contact=message.document)
    else:
        await state.update_data(contact=message.text)
        
    await state.set_state(Form.document)
    await message.answer(
        f"Ваше резюме",
        reply_markup=ReplyKeyboardRemove(),
    )

@form_router.message(Form.document)
async def process_name(message: Message, state: FSMContext) -> None:
    if message.document:
        if check_pdf(file_name=message.document.file_name):
            data = await state.update_data(document=message.document.file_id)
        else:
            await state.set_state(Form.document)
            await message.answer(
                'Перепрошую, але ми чекаємо на документ в форматі .pdf',
                reply_markup=ReplyKeyboardRemove(),
            )
            return
    else:
        await state.set_state(Form.document)
        await message.answer(
            f"Ваше резюме",
            reply_markup=ReplyKeyboardRemove(),
        )
        return

    await message.answer(
        "Давайте перевіримо чи все добре?",
        reply_markup=ReplyKeyboardRemove(),
    )
    await bot.send_document(
        message.chat.id,
        document=data.get('document'),
        caption=data.get('contact'),
        reply_markup=keyboard_approve()
    )
    '''
    await state.clear()
    await message.answer(
        f"Дякую",
        reply_markup=ReplyKeyboardRemove(),
    )
    await bot.send_message(
        GROUP_ID,
        text=data.get('contact')
        )
    await bot.send_document(
        GROUP_ID,
        document=data.get('document')
        )
    '''

@form_router.callback_query(func=lambda c: c == 'approve_false')
async def false_aproove(callback_query: CallbackQuery, state: FSMContext) -> None:
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Добре, почнемо все з початку')

async def main():
    dp = Dispatcher()
    
    dp.include_router(form_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
