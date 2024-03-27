from aiogram.utils.keyboard import KeyboardBuilder
from aiogram.types import KeyboardButton


startKeyboard = KeyboardBuilder()
startKeyboard.add(KeyboardButton(text="Получить заявку"))

doPlaceKeyboard = KeyboardBuilder()
doPlaceKeyboard.add(
    KeyboardButton("Изменить название места (название в рапорт)"),
    KeyboardButton("Изменить категорию места (категорию в рапорт)"),
    KeyboardButton("Изменить фильтры (фильтры в рапорт)"),
    KeyboardButton("Удалить место"),
    KeyboardButton("Заблокировать пользователя")
)

doReviewKeyboard = KeyboardBuilder()
doReviewKeyboard.add(
    KeyboardButton("Удалить отзыв"),
    KeyboardButton("Заблокировать пользователя")
)

cancelKeyboard = KeyboardBuilder()
cancelKeyboard.add(
    KeyboardButton("Назад к действиям")
)