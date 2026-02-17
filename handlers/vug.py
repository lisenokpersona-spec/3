from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from keyboards import ARCHETYPE_BUTTONS, create_keyboard
from states import TechTransition
from data import ARCHETYPE_NAMES

router = Router()

@router.callback_query(F.data.startswith('vug_'))
async def vug_chosen(callback: CallbackQuery, state: FSMContext):
    vug_code = callback.data.replace('vug_', '')
    vug_names = {
        'T-1': ' Командование',
        'T-2': ' Связь',
        'T-3': ' РЭБ / РЛС',
        'T-4': ' БПЛА',
        'T-5': ' Автобронетанк',
        'T-6': ' Инженерные',
        'T-7': ' Навигация',
        'T-8': ' Защита информации'
    }
    vug_name = vug_names.get(vug_code, vug_code)
    await state.update_data(vug=vug_code, vug_name=vug_name)
    
    await state.set_state(TechTransition.waiting_for_archetype)
    keyboard = create_keyboard(ARCHETYPE_BUTTONS)
    await callback.message.edit_text(
        "Выберите ваш архетип:\n\n"
        "Какой стиль управления и мышления вам ближе?",
        reply_markup=keyboard
    )
    await callback.answer()

@router.callback_query(F.data.startswith('arch_'))
async def archetype_chosen(callback: CallbackQuery, state: FSMContext):
    arch_code = callback.data.replace('arch_', '')
    arch_name = ARCHETYPE_NAMES.get(arch_code, arch_code)
    await state.update_data(archetype=arch_code, archetype_name=arch_name)
    
    from handlers.situations import send_situation_question
    await send_situation_question(callback.message, state, 1)
    await callback.answer()