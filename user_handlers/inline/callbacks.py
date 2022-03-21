import asyncio
import bot_items.messages_pack
import user_handlers.inline.inline_keyboard as inline_button
from database import user_memory

from loader import bot, dp, executor
from aiogram import types
from bot_items.config import admin_id
from bot_items.files_pack import icon_first_pack_labs, icon_second_pack_labs, icon_full_pack_labs


async def info_labs_constructor(callback_query: types.CallbackQuery, icon_pack, description_pack, inline_markup):
    chat_id = callback_query.message.chat.id
    await bot.answer_callback_query(callback_query.id)
    await asyncio.sleep(0.65)
    await bot.send_photo(chat_id, photo=icon_pack)
    await bot.send_message(chat_id, text=description_pack, reply_markup=inline_markup)


async def check_status_labs_pack(callback_query: types.CallbackQuery, pack_with_discount, classic_pack):
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id
    number_users = int(user_memory.sort_first_five_users())
    discount_state = 0

    if chat_id == admin_id:
        if number_users >= 7:
            discount_state * 0
            print(f"При отсутствии скидки: {discount_state}")
            print(f"Обнаружено превышение количества юзеров, для проведения скидки: {number_users}")
        elif number_users <= 6:
            discount_state += 30
            print(f"При скидке: {discount_state}")
            print(f"Обнаружено нужное количество юзеров, для проведения скидки: {number_users}")

    if discount_state == 30:
        await bot.edit_message_reply_markup(chat_id, message_id,
                                            reply_markup=pack_with_discount)
    else:
        await bot.edit_message_reply_markup(chat_id, message_id, reply_markup=classic_pack)

    await asyncio.sleep(30)
    await bot.send_message(chat_id, bot_items.messages_pack.send_pack_email_user)
    await asyncio.sleep(3)
    await bot.send_message(chat_id, bot_items.messages_pack.payback)


async def swipe_next_pack(callback_query: types.CallbackQuery, description_pack, next_keyboard_pack):
    await bot.answer_callback_query(callback_query.id)
    await asyncio.sleep(0.65)
    await callback_query.message.edit_text(text=description_pack,
                                           reply_markup=next_keyboard_pack)


@dp.callback_query_handler(lambda a: a.data == 'StartDialog')
async def callback_start(callback_query: types.CallbackQuery):
    number_users = int(user_memory.sort_first_five_users())
    await bot.answer_callback_query(callback_query.id)
    await asyncio.sleep(0.65)
    if number_users >= 11:
        await callback_query.message.edit_text(bot_items.messages_pack.start_button_text,
                                               reply_markup=inline_button.inline_packsLabs_full)
    elif number_users <= 10:
        await callback_query.message.edit_text(bot_items.messages_pack.price_discount_button_text,
                                               reply_markup=inline_button.inline_packsLabs_full)



@dp.callback_query_handler(lambda b: b.data == 'InfoFirstLabs')
async def callback_info_first_pack(callback_query: types.CallbackQuery):
    number_users = int(user_memory.sort_first_five_users())
    icon_pack = icon_first_pack_labs
    description_pack = bot_items.messages_pack.tm_description_first_pack
    inline_markup = inline_button.open_fl_dialog
    description_discount_pack = bot_items.messages_pack.tm_description_discount_first_pack
    if number_users >= 11:
        await info_labs_constructor(callback_query, icon_pack, description_pack, inline_markup)
    elif number_users <= 10:
        await info_labs_constructor(callback_query, icon_pack, description_discount_pack, inline_markup)



@dp.callback_query_handler(lambda c: c.data == 'InfoSecondLabs')
async def callback_info_second_pack(callback_query: types.CallbackQuery):
    number_users = int(user_memory.sort_first_five_users())
    icon_pack = icon_second_pack_labs
    description_pack = bot_items.messages_pack.tm_description_second_pack
    inline_markup = inline_button.open_sl_dialog
    description_discount_pack = bot_items.messages_pack.tm_description_discount_second_pack
    if number_users >= 11:
        await info_labs_constructor(callback_query, icon_pack, description_pack, inline_markup)
    elif number_users <= 10:
        await info_labs_constructor(callback_query, icon_pack, description_discount_pack, inline_markup)


@dp.callback_query_handler(lambda d: d.data == 'InfoFullLabs')
async def callback_info_full_pack(callback_query: types.CallbackQuery):
    number_users = int(user_memory.sort_first_five_users())
    icon_pack = icon_full_pack_labs
    description_pack = bot_items.messages_pack.tm_description_full_pack
    inline_markup = inline_button.open_fp_dialog
    description_discount_pack = bot_items.messages_pack.tm_description_discount_full_pack
    if number_users >= 11:
        await info_labs_constructor(callback_query, icon_pack, description_pack, inline_markup)
    elif number_users <= 10:
        await info_labs_constructor(callback_query, icon_pack, description_discount_pack, inline_markup)


@dp.callback_query_handler(lambda e: e.data == 'PaymentLinkFirstPL')
async def callback_check_status_first_pack(callback_query: types.CallbackQuery):
    pack_with_discount = inline_button.buy_fl_with_discount
    classic_pack = inline_button.buy_fl_dialog
    await check_status_labs_pack(callback_query, pack_with_discount, classic_pack)


@dp.callback_query_handler(lambda f: f.data == 'PaymentLinkSecondPL')
async def callback_check_status_second_pack(callback_query: types.CallbackQuery):
    pack_with_discount = inline_button.buy_sl_with_discount
    classic_pack = inline_button.buy_sl_dialog
    await check_status_labs_pack(callback_query, pack_with_discount, classic_pack)


@dp.callback_query_handler(lambda g: g.data == 'PaymentLinkFullPL')
async def callback_check_status_full_pack(callback_query: types.CallbackQuery):
    pack_with_discount = inline_button.buy_fp_with_discount
    classic_pack = inline_button.buy_fp_dialog
    await check_status_labs_pack(callback_query, pack_with_discount, classic_pack)


@dp.callback_query_handler(lambda i: i.data == 'NextPack')
async def callback_swipe_second_pack(callback_query: types.CallbackQuery):
    number_users = int(user_memory.sort_first_five_users())
    next_keyboard_pack = inline_button.open_sl_dialog
    description_pack = bot_items.messages_pack.tm_description_second_pack
    description_discount_pack = bot_items.messages_pack.tm_description_discount_second_pack

    if number_users >= 11:
        await swipe_next_pack(callback_query, description_pack, next_keyboard_pack)
    elif number_users <= 10:
        await swipe_next_pack(callback_query, description_discount_pack, next_keyboard_pack)


@dp.callback_query_handler(lambda k: k.data == 'MediumPreviousPack')
async def callback_swipe_previous_pack(callback_query: types.CallbackQuery):
    number_users = int(user_memory.sort_first_five_users())
    next_keyboard_pack = inline_button.open_fl_dialog
    description_pack = bot_items.messages_pack.tm_description_first_pack
    description_discount_pack = bot_items.messages_pack.tm_description_discount_first_pack

    if number_users >= 11:
        await swipe_next_pack(callback_query, description_pack, next_keyboard_pack)
    elif number_users <= 10:
        await swipe_next_pack(callback_query, description_discount_pack, next_keyboard_pack)


@dp.callback_query_handler(lambda n: n.data == 'MediumNextPack')
async def callback_swipe_full_pack(callback_query: types.CallbackQuery):
    number_users = int(user_memory.sort_first_five_users())
    next_keyboard_pack = inline_button.open_fp_dialog
    description_pack = bot_items.messages_pack.tm_description_full_pack
    description_discount_pack = bot_items.messages_pack.tm_description_discount_full_pack

    if number_users >= 11:
        await swipe_next_pack(callback_query, description_pack, next_keyboard_pack)
    elif number_users <= 10:
        await swipe_next_pack(callback_query, description_discount_pack, next_keyboard_pack)


@dp.callback_query_handler(lambda m: m.data == 'LastPreviousPack')
async def callback_swipe_previous_second_pack(callback_query: types.CallbackQuery):
    await callback_swipe_second_pack(callback_query)


@dp.callback_query_handler(lambda l: l.data == 'Load')
async def process_download(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await asyncio.sleep(0.65)
    await callback_query.message.edit_text(bot_items.messages_pack.download_button_text,
                                           reply_markup=inline_button.download_dialog)
    await asyncio.sleep(0.65)
    await callback_query.message.edit_text(bot_items.messages_pack.failed_load_button_text,
                                           reply_markup=inline_button.download_dialog)
    await asyncio.sleep(0.65)
    await callback_query.message.edit_text(bot_items.messages_pack.upload_button_text,
                                           reply_markup=inline_button.download_dialog)
    await asyncio.sleep(0.65)
    await callback_query.message.edit_text(bot_items.messages_pack.done_load_button_text,
                                           reply_markup=inline_button.download_dialog)
    await asyncio.sleep(0.65)
    await callback_info_first_pack(callback_query)


@dp.callback_query_handler(lambda h: h.data == 'InfoDev')
async def process_dev_project_roadmap(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    await asyncio.sleep(0.65)
    await bot.send_message(chat_id, bot_items.messages_pack.projects_in_progress)


@dp.callback_query_handler(lambda g: g.data == 'CheckPayment')
async def process_check_payment_status(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id

