from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import db


def make_product_keyboard(category_name: str):
    products = db.get_products_by_category_name(category_name)
    buttons = []

    menu = ReplyKeyboardMarkup(keyboard=[], resize_keyboard=True, row_width=2)
    
    for product in products:
        buttons.append(
            KeyboardButton(text=product[0])
        )

    menu.keyboard.append(
        buttons
    )

    return menu
