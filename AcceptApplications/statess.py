from aiogram.dispatcher.filters.state import State, StatesGroup

class NewUserForm(StatesGroup):
    time = State()
    # info = State()
    experience = State()