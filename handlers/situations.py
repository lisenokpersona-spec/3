from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from keyboards import SITUATION_BUTTONS, create_keyboard
from states import TechTransition

router = Router()

SITUATION_QUESTIONS = {
    1: (
        "❓ Ситуация 1/5: Управление проектами\n\n"
        "Справляетесь ли вы с планированием и контролем проектов в срок?"
    ),
    2: (
        "❓ Ситуация 2/5: Управление людьми\n\n"
        "Есть ли у вас опыт руководства командой (наставничество, распределение задач)?"
    ),
    3: (
        "❓ Ситуация 3/5: Техническая экспертиза\n\n"
        "Глубоко ли вы разбираетесь в технической части своей предметной области?"
    ),
    4: (
        "❓ Ситуация 4/5: Коммуникации\n\n"
        "Умеете ли вы убеждать, согласовывать, доносить сложное простыми словами?"
    ),
    5: (
        "❓ Ситуация 5/5: Стрессоустойчивость\n\n"
        "Сохраняете ли вы эффективность в условиях неопределённости и давления?"
    )
}

async def send_situation_question(message: Message, state: FSMContext, num: int):
    state_map = {
        1: TechTransition.waiting_for_situation_1,
        2: TechTransition.waiting_for_situation_2,
        3: TechTransition.waiting_for_situation_3,
        4: TechTransition.waiting_for_situation_4,
        5: TechTransition.waiting_for_situation_5,
    }
    await state.set_state(state_map[num])
    keyboard = create_keyboard(SITUATION_BUTTONS, row_width=3)
    await message.edit_text(SITUATION_QUESTIONS[num], reply_markup=keyboard)

@router.callback_query(F.data.startswith('situ_'))
async def process_situation(callback: CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    
    state_to_num = {
        TechTransition.waiting_for_situation_1: 1,
        TechTransition.waiting_for_situation_2: 2,
        TechTransition.waiting_for_situation_3: 3,
        TechTransition.waiting_for_situation_4: 4,
        TechTransition.waiting_for_situation_5: 5,
    }
    
    current_num = state_to_num.get(current_state)
    if not current_num:
        await callback.answer("Ошибка состояния", show_alert=True)
        return
    
    answer = callback.data.replace('situ_', '')
    answer_text = {
        'yes': '✅ Да',
        'part': '⚠️ Частично',
        'no': '❌ Нет'
    }.get(answer, answer)
    
    # Сохраняем ответ
    data = await state.get_data()
    situations = data.get('situations', {})
    situations[current_num] = {
        'code': answer,
        'text': answer_text
    }
    await state.update_data(situations=situations)
    
    if current_num < 5:
        await send_situation_question(callback.message, state, current_num + 1)
    else:
        # Переходим к результатам
        from handlers.result import show_results
        await show_results(callback.message, state)
    
    await callback.answer()