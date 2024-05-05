from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import KeyboardButton, InlineKeyboardButton


startKeyboard = ReplyKeyboardBuilder(
    [[KeyboardButton(text="Получить заявку")]]
).as_markup()


doPlaceKeyboard = InlineKeyboardBuilder(
    markup=[
        [InlineKeyboardButton(text="Изменить название", callback_data="data")],
        [InlineKeyboardButton(text="Изменить категорию", callback_data="data")],
        [InlineKeyboardButton(text="Изменить фильтры", callback_data="data")],
        [
            InlineKeyboardButton(text="Удалить", callback_data="data"), 
            InlineKeyboardButton(text="Забанить", callback_data="data")
        ]
    ]
).as_markup()


doReviewKeyboard = InlineKeyboardBuilder(
    [[
        InlineKeyboardButton(text="Удалить", callback_data="data"),
        InlineKeyboardButton(text="Забанить", callback_data="data")
    ]]
).as_markup()


cancelKeyboard = InlineKeyboardBuilder(
    [[InlineKeyboardButton(text="Назад к действиям", callback_data="data")]]
).as_markup()