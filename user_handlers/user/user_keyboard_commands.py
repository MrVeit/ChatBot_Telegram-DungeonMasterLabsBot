import asyncio
import bot_items.messages_pack
import user_handlers.user.user_keyboard as keyboard
import user_handlers.inline.inline_keyboard as inline_button
from database import user_memory

from loader import bot, dp, executor
from aiogram import types
from aiogram.types import ChatActions
from aiogram.utils.markdown import hide_link


@dp.message_handler(lambda message: message.text == "Прайс-лист 📝")
async def price_list_command(message: types.Message):
    number_users = int(user_memory.sort_first_five_users())

    if number_users >= 11:
        await message.answer(bot_items.messages_pack.start_button_text, reply_markup=inline_button.inline_packsLabs_full)
    elif number_users <= 10:
        await message.answer(bot_items.messages_pack.price_discount_button_text, reply_markup=inline_button.inline_packsLabs_full)


@dp.message_handler(lambda message: message.text == "Купить пак лаб 💸")
async def load_labs_command(message: types.Message):
    await message.answer(bot_items.messages_pack.load_button_text, reply_markup=inline_button.load_dialog)


@dp.message_handler(lambda message: message.text == "Обратная связь 🆘")
async def feedback_command(message: types.Message):
    await message.answer(bot_items.messages_pack.feedback_message, reply_markup=keyboard.feedback_markup)


@dp.message_handler(lambda message: message.text == "Разработчик 🧑🏾‍💻")
async def developer_command(message: types.Message):
    await message.answer(f"{hide_link('https://github.com/MrVeit')}"
                         f"Итак, ну и какого-то хера ты решил сюда кликнуть, "
                         f"странный человечешка 🧐 \n\nНу раз так, то чего лишним байтам пропадать,"
                         f" вот держи несколько ссылок на моего создателя:"
                         , parse_mode=types.ParseMode.HTML, reply_markup=inline_button.dev_dialog)


@dp.message_handler(lambda message: message.text == "Отправить отзыв 👺")
async def apply_review_command(message: types.Message):
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.UPLOAD_VIDEO_NOTE)
    await asyncio.sleep(0.65)
    await bot.send_video(user_id, open('files/gop_stop.mp4', 'rb'))
    await message.answer("Ваш отзыв был успешно отправлен (в корзину) 🌚", reply_markup=keyboard.main_markup)

