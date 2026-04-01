from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    kb = [
        [KeyboardButton(text="1. Kassa amaliyotlari"), KeyboardButton(text="2. Kartaga xizmat")],
        [KeyboardButton(text="3. Pul o'tkazmalari"), KeyboardButton(text="4. Kreditlar")],
        [KeyboardButton(text="5. Depozitlar"), KeyboardButton(text="6. Hisob-kitoblar")],
        [KeyboardButton(text="7. Boshqa xizmatlar")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


def sub_menu(category):
    menus = {
        "1": ["Naqd pul kiritish", "Naqd pul olish", "Valyuta ayirboshlash", "To'lovlar"],
        "2": ["Kartani yangilash", "Blokdan ochish", "PIN-kod o'zgartirish"],
        "3": ["SQB o'tkazma", "Western Union", "MoneyGram", "Zolotaya Korona"],
        "4": ["Iste'mol krediti", "Kredit тўlovi", "Kredit maslahati"],
        "5": ["Depozit ochish", "Foizlarni olish"],
        "6": ["Ko'chirma olish", "Hisob raqam ochish"],
        "7": ["Ipoteka maslahati", "Yuridik shaxslar", "Ko'makchi xodim"]
    }

    buttons = []
    items = menus.get(category, [])
    # Tugmalarni 2 tadan qatorga teramiz
    for i in range(0, len(items), 2):
        row = [KeyboardButton(text=items[i])]
        if i + 1 < len(items):
            row.append(KeyboardButton(text=items[i + 1]))
        buttons.append(row)

    buttons.append([KeyboardButton(text="⬅️ Orqaga")])
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)