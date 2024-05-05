from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, StateFilter
from aiogram.filters.magic_data import MagicData

from src.client import SportacusClient

from src.config import (
    MODERATOR_ID, BASE_URL, MODERATOR_KEY, FRONTEND_URL
)
from aiogram import F
from .keyboards.keyboard import (
    startKeyboard, cancelKeyboard,
    doPlaceKeyboard, doReviewKeyboard
)
from .FSM.fsm import Form

dp = Dispatcher()
dp.message.filter(MagicData(F.event_from_user.id == MODERATOR_ID))

client = SportacusClient(BASE_URL, MODERATOR_KEY)


@dp.message(CommandStart())
async def start(message: Message): 
    return await message.answer(
        "Получите заявку по кнопке", reply_markup=startKeyboard
    )

@dp.message(F.text.lower() == "получить заявку")
async def mark(message: Message): 
    resp = await client.moderate.get()
    link = f"{FRONTEND_URL}/{resp.item.place_id}"

    keyb = None
    if resp.type == "PLACE":
        keyb = doPlaceKeyboard
    else: keyb = doReviewKeyboard

    await message.answer(
        f"Ссылка на место: {link}\nПричина: {resp.cause}\nКол-во жалоб на пользователя: {resp.complaint_count}\n\nВыберите действие ниже:",
        reply_markup=keyb
    )

@dp.callback_query()
async def report(message: Message): 
    await message.answer(
        "", reply_markup=startKeyboard
    )

@dp.message()
async def cancel(message: Message): 
    await message.answer(
        "", reply_markup=startKeyboard
    )
