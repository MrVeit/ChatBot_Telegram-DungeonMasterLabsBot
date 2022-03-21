from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_button = InlineKeyboardButton('Посмотреть актуальный прайс-лист 💸',
                                    callback_data='StartDialog')
info_1st_labs_button = InlineKeyboardButton('Пак "Новичок" 🍼',
                                            callback_data='InfoFirstLabs')
info_2st_labs_button = InlineKeyboardButton('Пак "Fucking slave" 👨🏼‍🦽',
                                            callback_data='InfoSecondLabs')
info_full_labs_button = InlineKeyboardButton('Пак "Dungeon master" ♂️',
                                             callback_data='InfoFullLabs')
buy_1st_labs_button = InlineKeyboardButton('Купить за 1990 RUB 🍼',
                                           url='https://payok.io/payment_link/98vw1-fdmrr-45m57')
buy_2st_labs_button = InlineKeyboardButton('Купить за 2990 RUB 👨🏼‍🦽',
                                           url='https://payok.io/payment_link/e6342-5t7p0-080df')
buy_full_labs_button = InlineKeyboardButton('Купить за 4490 RUB ♂',
                                            url='https://payok.io/payment_link/s9335-y5rwc-m6q6f')
buy_with_30_discount_1st_labs_button = InlineKeyboardButton('Купить за 995 RUB 🍼',
                                                            url='https://payok.io/payment_link/cl95w-5r920-jfk75')
buy_with_30_discount_2st_labs_button = InlineKeyboardButton('Купить за 1495 RUB 👨🏼‍🦽',
                                                            url='https://payok.io/payment_link/h11kn-6e977-s0a53')
buy_with_30_discount_full_labs_button = InlineKeyboardButton('Купить за 2245 RUB ♂',
                                                             url='https://payok.io/payment_link/80x3d-1a37a-mswh7')
feedback_button = InlineKeyboardButton('Обратная связь 📝',
                                       callback_data='FeedBack')
dev_button = InlineKeyboardButton('GitHub 🧸',
                                  url='https://github.com/MrVeit')
first_game_button = InlineKeyboardButton('Первый pet-проект 🤖',
                                         url='https://play.google.com/store/apps/'
                                             'details?id=com.Veiteriogames.vellstory')
dev_acc_button = InlineKeyboardButton('Аккаунт разработчика 🎮',
                                      url='https://play.google.com/store/apps/'
                                          'dev?id=8989430577205514684')
projects_in_progress_button = InlineKeyboardButton('Разрабатываемые проекты ⚙️', callback_data='InfoDev')
next_pack_labs = InlineKeyboardButton('Следующий набор ➡️',
                                      callback_data='NextPack')
medium_next_pack_labs = InlineKeyboardButton('Следующий набор ➡️',
                                             callback_data='MediumNextPack')
medium_previous_pack_labs = InlineKeyboardButton(' ⬅️ Предыдущий набор',
                                                 callback_data='MediumPreviousPack')
last_previous_pack_labs = InlineKeyboardButton(' ⬅️ Предыдущий набор',
                                               callback_data='LastPreviousPack')
load_button = InlineKeyboardButton('Вмешаться 🤬',
                                   callback_data='Load')
download_button = InlineKeyboardButton('Загрузка ⏳',
                                       callback_data='Download')
get_payment_link_first_pack = InlineKeyboardButton('Приобрести пак "Новичок" 🍼',
                                                   callback_data='PaymentLinkFirstPL')
get_payment_link_second_pack = InlineKeyboardButton('Приобрести пак "Fucking slave" 👨🏼‍🦽',
                                                    callback_data='PaymentLinkSecondPL')
get_payment_link_full_pack = InlineKeyboardButton('Приобрести пак "Dungeon master" ♂️',
                                                  callback_data='PaymentLinkFullPL')

start_dialog = InlineKeyboardMarkup().add(start_button)
info_fl_dialog = InlineKeyboardMarkup().add(info_1st_labs_button)
info_sl_dialog = InlineKeyboardMarkup().add(info_2st_labs_button)
info_fp_dialog = InlineKeyboardMarkup().add(info_full_labs_button)
open_fl_dialog = InlineKeyboardMarkup().add(get_payment_link_first_pack).add(next_pack_labs)
open_sl_dialog = InlineKeyboardMarkup().add(get_payment_link_second_pack).row(medium_previous_pack_labs,
                                                                              medium_next_pack_labs)
open_fp_dialog = InlineKeyboardMarkup().add(get_payment_link_full_pack).add(last_previous_pack_labs)
buy_fl_dialog = InlineKeyboardMarkup().add(buy_1st_labs_button).add(next_pack_labs)
buy_sl_dialog = InlineKeyboardMarkup().add(buy_2st_labs_button).row(medium_previous_pack_labs, medium_next_pack_labs)
buy_fp_dialog = InlineKeyboardMarkup().add(buy_full_labs_button).add(last_previous_pack_labs)
buy_fl_with_discount = InlineKeyboardMarkup().add(buy_with_30_discount_1st_labs_button).add(next_pack_labs)
buy_sl_with_discount = InlineKeyboardMarkup().add(buy_with_30_discount_2st_labs_button).row(medium_previous_pack_labs,
                                                                                            medium_next_pack_labs)
buy_fp_with_discount = InlineKeyboardMarkup().add(buy_with_30_discount_full_labs_button).add(last_previous_pack_labs)
next_pack_dialog = InlineKeyboardMarkup().add(next_pack_labs)
load_dialog = InlineKeyboardMarkup().add(load_button)
download_dialog = InlineKeyboardMarkup().add(download_button)

dev_dialog = InlineKeyboardMarkup(row_width=1).add(dev_button).row(first_game_button, dev_acc_button)\
    .add(projects_in_progress_button)
inline_packsLabs_full = InlineKeyboardMarkup(row_width=1).add(info_1st_labs_button,
                                                              info_2st_labs_button, info_full_labs_button)
inline_buy_pack_labs_full = InlineKeyboardMarkup(row_width=1).add(buy_1st_labs_button,
                                                                  buy_2st_labs_button, buy_full_labs_button)
inline_keyboard_full = InlineKeyboardMarkup(row_width=2).add(feedback_button, dev_button)
