from loader import executor, loop
from user_handlers.user import dp
from user_handlers.inline import dp
from user_handlers.any import dp


def start_bot():
    executor.start_polling(dp, loop=loop, skip_updates=True)


if __name__ == '__main__':
    start_bot()

