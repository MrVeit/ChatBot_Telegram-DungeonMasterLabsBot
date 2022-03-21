import asyncio
import bot_items.messages_pack

import user_handlers.user.user_keyboard as keyboard
import user_handlers.inline.inline_keyboard as inline_button
from database import user_memory

from loader import bot, dp, executor
from aiogram import types
from aiogram.types import ChatActions
from bot_items.config import admin_id
from bot_items.files_pack import sticker_dev_matrix, sticker_ubivan


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    user_id = message.from_user.id
    full_name_user = str(message.from_user.username)
    user_memory.create_users_database(message)
    await message.answer(f"Я вас категорически приветствую, @*{full_name_user}* 👺",
                         reply_markup=keyboard.main_markup)
    await bot.send_chat_action(user_id, ChatActions.UPLOAD_VIDEO_NOTE)
    await asyncio.sleep(0.65)
    await bot.send_video(user_id, open('files/gacha_hi.mp4', 'rb'))
    await message.answer(bot_items.messages_pack.start_message, reply_markup=inline_button.start_dialog)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.CHOOSE_STICKER)
    await asyncio.sleep(0.65)
    await bot.send_sticker(user_id, sticker_dev_matrix)
    await message.answer(bot_items.messages_pack.help_message, reply_markup=inline_button.inline_packsLabs_full)


@dp.message_handler(commands=['stat'])
async def load_stat(message: types.Message):
    chat_id = message.chat.id
    current_users = user_memory.sort_current_users()

    if chat_id == admin_id:
        await message.answer(f'⚙️ Авторизованные пользователи системы Master Labs:'
                             f'\n\n| Порядковый номер | Идентификатор TG | Никнейм |'
                             f'\n\n*{current_users}*')
    else:
        await message.answer(f'Ошибка доступа, на данный момент,'
                             f'ваш статус в системе: *fucking slave 🌚*')


@dp.message_handler(commands=['mail'])
async def mailing_list(message: types.Message):
    chat_id = message.chat.id
    bad_chars = ['/', 'm', 'a', 'i', 'l']
    id_users = user_memory.read_current_users()
    current_message = message.text[message.text.find(''):]
    current_message = filter(lambda t: t not in bad_chars, current_message)
    message_for_users = "".join(current_message)

    if chat_id == admin_id:
        await bot.send_message(chat_id, f"*Рассылка началась 🧸 "
                                        f"\n\nБот оповестит, когда рассылку закончит!*")
        receive_users = 0
        block_users = 0

        for user in range(len(id_users)):
            try:
                await bot.send_message((id_users[user][0]), message_for_users)
                receive_users += 1
            except:
                block_users += 1
            await asyncio.sleep(0.65)
        await bot.send_message(chat_id, f"*Рассылка завершена успешно! 🥳*\n\n"
                                        f"Получили сообщения: *{receive_users}* slaves ✅\n"
                                        f"Заблокировали бота: *{block_users}* assholes ❌")


@dp.message_handler(commands=['remove'])
async def remove_command(message: types.Message):
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.CHOOSE_STICKER)
    await asyncio.sleep(0.65)
    await bot.send_sticker(user_id, sticker_ubivan)
    await message.answer('Так держать! \nВы только что сломали казённую клавиатуру за 40 гривен! 😿',
                         reply_markup=keyboard.ReplyKeyboardRemove())
