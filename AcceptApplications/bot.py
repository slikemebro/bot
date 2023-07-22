# -*- coding: utf-8 -*-
import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.handler import current_handler, CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import Throttled

import config
import menu
from statess import *

# config_name = "config.ini"

bot = Bot(config.API_BOT, parse_mode='HTML')

dp = Dispatcher(bot,storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)
bd = 'data/database.db'

reported_users = {}
GROUP_ID = 531368227
REPORT_ID = 531368227
REPORT_TIME = 15 * 60

print('Воркер бот успешно запущен [+]')


@dp.message_handler(commands="start", state='*')
async def start(message: types.Message):
    await message.answer('🍀 Добро пожаловать в ICloudTeam', reply_markup=menu.prinsogl)


@dp.callback_query_handler(text='rules')
async def registration(call: CallbackQuery):
    await call.message.answer(f'🛠️ Для работы с нами, потребуется заполонить анкету.', parse_mode='HTML')
    await call.message.answer("<b>Откуда Вы узнали о нас?</b>\nНапример: реклама в @TelegramChanel. Или пригласил @username", parse_mode='HTML')
    await NewUserForm.time.set()


@dp.message_handler(state=NewUserForm.time)
async def answer_time(message: types.Message, state: FSMContext):
    await state.update_data(time=message.text)
    await message.answer("<b>Был ли опыт и где?</b>\nНапример: 2 месяца в нфт, воркал в … Тиме", parse_mode='HTML')
    await NewUserForm.next()

# @dp.message_handler(state=NewUserForm.info)
# async def answer_time(message: types.Message, state: FSMContext):
#     await state.update_data(info=message.text)
#     await message.answer("<b>Сколько времени Вы готовы уделять работе в проекте?</b>", parse_mode='HTML')
#     await NewUserForm.next()

@dp.message_handler(state=NewUserForm.experience)
async def answer_exp(message: types.Message, state: FSMContext):
    await state.update_data(exp=message.text)
    data = await state.get_data()
    await message.answer(f"🖨️ <b>Ваша заявка была успешно отправлена администрации команды</b>\n\n⏳Примерное рассмотрение ~ 3 часа")
    if message.from_user.username:
        username = f'@{message.from_user.username}'
    else:
        username = message.from_user.first_name
    # try:
        # ref = int(data.get('time'))
    # except:
    #     ref = 0
    await bot.send_message(GROUP_ID, f"<b>Поступила заявка от @{message.from_user.username}\n</b>"
                                  f"ID: <b>{message.from_user.id}</b>\n\n"
                                  # f"1. <b>{data.get('time')}</b>\n"
                                  f"1. <b>{data.get('exp')}</b>\n"
                                  f"2. <b>{data.get('info')}</b>\n",reply_markup=menu.admin_pick(username, message.from_user.id, 0))
    await state.finish()


@dp.callback_query_handler(menu.user_info_callback.filter(status='1'))
async def accept_form(call: CallbackQuery, callback_data: dict):
    await call.bot.edit_message_text(call.message.text + f"\n\n✅ Заявка одобрена {callback_data.get('username')}",
                                     call.message.chat.id, call.message.message_id)
    await call.bot.send_message(callback_data.get("user_id"), '🥳')
    await call.bot.send_message(callback_data.get("user_id"),
                                '🔒 <b>Администрация рассмотрела вашу заявку. Вы были приняты в команду.</b>\n\nВступайте в чат и начинайте работать!\n<b>Удачных профитов!</b>',
                                reply_markup=menu.links, parse_mode='HTML')

    # with sqlite3.connect(bd) as c:
    #     c.execute('INSERT INTO workers VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (
    #     callback_data.get("user_id"), callback_data.get('username'), random.randint(79023457654, 79869999999),
    #     random.randint(000000, 999999), '0', '0', '1000', random.randint(5536910000000000, 5536919999999999), '0', '0',
    #     '0', '0', '0', '0', callback_data.get('ref'), datetime.now().strftime("%d.%m.%Y %H:%M:%S"), '0'))
    #     c.execute('UPDATE stat SET workers = workers + ? WHERE nice = ?', ('1', '777',))


@dp.callback_query_handler(menu.user_info_callback.filter(status='0'))
async def decline_form(call: CallbackQuery, callback_data: dict):
    await call.bot.edit_message_text(call.message.text + f"\n\n🛑 Заявка была отклонена администрацией. {callback_data.get('username')}",
                                     call.message.chat.id, call.message.message_id)
    await call.bot.send_message(callback_data.get("user_id"), "<b>🛑 Ваша заявка была отклонена.</b>", parse_mode='HTML')


executor.start_polling(dp)