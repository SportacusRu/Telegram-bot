from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.state import State, StatesGroup

class Form(StatesGroup):
    report = State()  # Will be represented in storage as 'Form:name'
