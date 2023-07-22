from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
import config

user_info_callback = CallbackData("user_reg","ref", "status", "username", "user_id")


prinsogl = InlineKeyboardMarkup(
	inline_keyboard = [
        [
            InlineKeyboardButton(text='✅ Продолжить', callback_data='rules')
		]
	]
)

def admin_pick(username, user_id, ref):
    print(username,user_id,ref)
    accept = InlineKeyboardButton(text='Подтвердить', callback_data=user_info_callback.new(ref = ref,status=1, username=username,user_id=user_id))
    decline = InlineKeyboardButton(text='Отклонить', callback_data=user_info_callback.new(ref = ref,status=0, username=username,user_id=user_id ))
    return InlineKeyboardMarkup().add(accept, decline)

mainkb = ReplyKeyboardMarkup(
    resize_keyboard=True,
	keyboard = [
		[
            KeyboardButton(text='Профиль 📁')
		],
        [
            KeyboardButton(text='Арбитраж 🌐'),
            KeyboardButton(text='Казино 🎰')
        ],
        [
            KeyboardButton(text='Трейдинг 📈')
        ],
        [
            KeyboardButton(text='О проекте 👨‍💻')
		]
	]
)

links = InlineKeyboardMarkup(
	inline_keyboard = [
        [
            InlineKeyboardButton(text='Чат воркеров ‍👨‍💻', url='https://t.me/+7AauHFU6dw9kY2U6')
        ],
        [
            InlineKeyboardButton(text='Канал выплат 💸', url='https://t.me/+PiHh4IvJB4QzNzY6')
		],
        [
            InlineKeyboardButton(text='Голосовые для ворка ', url='https://t.me/+sxTzDmSAtgY3MWQy')
        ],
        [
            InlineKeyboardButton(text='Отзывы ', url='https://t.me/+WtPxX8caGXwwMmY6')
        ],
        [
            InlineKeyboardButton(text='Помощник ', url='https://t.me/+Tdl_GRuAyphiY2Yy')
        ],
        [
            InlineKeyboardButton(text='Мануалы 📑', url='https://t.me/+ovxrXIe1VpxiMzNi')
		]
	]
)