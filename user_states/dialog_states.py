from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from  aiogram import types
from loader import dp


available_review_models = ["Обратная связь 🆘", "Фидбэк", "Отзыв"]
available_get_products = ["Получить товар", "Забрать набор"]


class DialogModels(StatesGroup):
    waiting_for_review_model = State()
    waiting_for_get_product = State()

@dp.message_handler(commands=['review'])
async def review_start(message: types.Message):
    await message.answer("Выберите режим диалога:")
    await DialogModels.waiting_for_review_model.set()


async def review_chosen(message: types.Message, state: FSMContext):
    if message.text.lower() not in available_review_models:
        await message.answer("Напишите корректный запрос для получения меню 'Отзывы'")
        return
    await state.update_data(chosen_review=message.text.lower())
    await state.finish()


@dp.message_handler(command=['product'])
async def product_start(message: types.Message):
    await message.answer("Выберите способ получения товарa:")
    await DialogModels.waiting_for_get_product.set()


async def product_chosen(message: types.Message, state: FSMContext):
    if message.text.lower() not in available_get_products:
        await message.answer("Напишите корректный запрос для получения меню 'Получение товара'")
        return
    await state.update_data(chosen_producct=message.text.lower())
    await state.finish()