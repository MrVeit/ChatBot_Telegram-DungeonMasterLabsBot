from aiogram.types import ReplyKeyboardMarkup, \
    KeyboardButton, ReplyKeyboardRemove

price_list_button = KeyboardButton('Прайс-лист 📝')
pack_labs_button = KeyboardButton('Купить пак лаб 💸')
feedback_button = KeyboardButton('Обратная связь 🆘')
dev_info_button = KeyboardButton('Разработчик 🧑🏾‍💻')
send_review_button = KeyboardButton('Отправить отзыв 👺')

main_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)\
    .row(price_list_button, pack_labs_button)\
    .add(feedback_button, dev_info_button)

feedback_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)\
    .row(send_review_button)
