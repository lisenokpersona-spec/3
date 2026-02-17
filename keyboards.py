from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

VUG_BUTTONS = [
    ('Т‑1 Командование', 'vug_T-1'),
    ('Т‑2 Связь', 'vug_T-2'),
    ('Т‑3 РЭБ / РЛС', 'vug_T-3'),
    ('Т‑4 БПЛА', 'vug_T-4'),
    ('Т‑5 Автобронетанк', 'vug_T-5'),
    ('Т‑6 Инженерные', 'vug_T-6'),
    ('Т‑7 Навигация', 'vug_T-7'),
    ('Т‑8 Защита информации', 'vug_T-8')
]

ARCHETYPE_BUTTONS = [
    ('А — Управленец (организую процессы)', 'arch_A'),
    ('Б — Технократ (строю архитектуру)', 'arch_B'),
    ('В — Аналитик (контролирую риски)', 'arch_C')
]

SITUATION_BUTTONS = [
    ('✅ Да, справляюсь', 'situ_yes'),
    ('⚠️ Частично, есть пробелы', 'situ_part'),
    ('❌ Нет, не сталкивался', 'situ_no')
]

ROADMAP_BUTTONS = [
    ('🚀 Корпоративная карьера', 'road_go_corp'),
    ('🔧 Интегратор / Подрядчик', 'road_integrator'),
    ('💡 Свой стартап', 'road_startup')
]

def create_keyboard(buttons: list, row_width: int = 1) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for text, callback in buttons:
        builder.add(InlineKeyboardButton(text=text, callback_data=callback))
    builder.adjust(row_width)
    return builder.as_markup()
