from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F
from utils import get_parse_data
from aiogram.utils.keyboard import InlineKeyboardBuilder
import text


router = Router()


@router.message(Command("start"))
async def start_handler(message: types.Message):
    kb = [[types.KeyboardButton(text="get data")],]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    print(message.entities)
    await message.answer(
        text.greet.format(name=message.from_user.full_name),
        reply_markup=keyboard
    )


@router.message(Command("data"))
async def start_handler(message: types.Message):
    print(message.entities)
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="get data",
        callback_data="data"
    )
    )
    await message.answer(
        text.greet.format(name=message.from_user.full_name),
        reply_markup=builder.as_markup()
    )


@router.message(F.text.lower() == "get data")
async def get_data(message: types.Message):
    result = get_parse_data()
    print(result[0], result[1])
    print(message.entities)
    await message.reply(f"{result[0]} {result[1]}")


@router.callback_query(F.data == "data")
async def callback_data(callback: types.CallbackQuery):
    result = get_parse_data()
    print(result[0], result[1])
    # print(callback.message.entities)
    await callback.message.answer(f"{result[0]} {result[1]}")
    await callback.answer(
        text=f"{result[0]} {result[1]}",
        show_alert=True
    )

# @router.message(F.text)
# async def echo(message: types.Message):
#     entities = message.entities or []
#     for item in entities:
#         print(item.extract_from(message.text))
#         await message.answer(item.extract_from(message.text))
