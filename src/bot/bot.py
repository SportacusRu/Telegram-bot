from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, StateFilter

from src.config import TOKEN, MODERATOR_ID
from aiogram import MagicData, F
from .keyboards.keyboard import (
    startKeyboard, cancelKeyboard,
    doPlaceKeyboard, doReviewKeyboard
)
from .FSM.fsm import Form

dp = Dispatcher()
dp.update.filter(MagicData(F.event_from_user.id == MODERATOR_ID))


@dp.message(CommandStart())
async def start(message: Message): 
    return await message.answer(
        "Получите заявку по кнопке", reply_markup=startKeyboard
    )

@dp.message()
async def mark(message: Message): 
    await message.answer(
        "", reply_markup=startKeyboard
    )

@dp.message()
async def report(message: Message): 
    await message.answer(
        "", reply_markup=startKeyboard
    )

@dp.message()
async def cancel(message: Message): 
    await message.answer(
        "", reply_markup=startKeyboard
    )
