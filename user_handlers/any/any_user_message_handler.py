from loader import bot, dp, executor
from aiogram import types
from bot_items.config import admin_id
from aiogram.utils.markdown import text
from aiogram.utils.emoji import emojize
from aiogram.dispatcher import FSMContext
from aiogram.types.message import ContentType


@dp.message_handler(content_types=ContentType.TEXT)
async def send_review_command(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    if message.text != "Отправить отзыв 👺":
        await bot.send_message(admin_id, f"⚠️ Новый отзыв: {message.text} \n"
                                            f"от пользователя: {user_id}")
        await state.reset_state()
    else:
        return


@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(message: types.Message):
    message_text = text(emojize('Ты чего наделал? :astonished:'),
                        text('\n\n''Ты давай, лучше убери тут за собой', 'и не мешай' '\n' 'мне работать! 😼',
                             '\n''Ну и на всякий случай напомню, что у меня доступны только следующие команды:',
                             '/start', ',' ' ' '/help'))
    await message.reply(message_text)
