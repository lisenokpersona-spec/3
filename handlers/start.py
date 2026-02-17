from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from keyboards import VUG_BUTTONS, create_keyboard

router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "⚡ ТОЧКА ТЕХНОЛОГИЧЕСКОГО ПЕРЕХОДА ⚡\n\n"
        "Вы — профессионал с уникальным опытом. Сейчас вы находитесь на пороге кардинальных перемен.\n"
        "Этот бот поможет вам найти ТОЧКУ ОПОРЫ в гражданской техносфере.\n\n"
        "За 5 минут вы узнаете:\n"
        "• Ваши родственные гражданские специальности (технологическое лидерство)\n"
        "• Как конвертировать военные компетенции\n"
        "• Персональную дорожную карту развития\n\n"
        "Нажмите /next, чтобы начать."
    )

@router.message(Command('next'))
async def cmd_next(message: Message, state: FSMContext):
    from states import TechTransition
    await state.set_state(TechTransition.waiting_for_vug)
    keyboard = create_keyboard(VUG_BUTTONS, row_width=2)
    await message.answer(
        "Выберите вашу военно-учётную группу (ВУГ):\n\n"
        "Это определит вектор перехода в технологическом секторе.",
        reply_markup=keyboard
    )