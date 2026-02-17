from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from data import ROADMAPS, CONVERSION_EXAMPLES

router = Router()

@router.callback_query(F.data.startswith('road_'))
async def roadmap_chosen(callback: CallbackQuery, state: FSMContext):
    road_key = callback.data.split('_')[1]
    roadmap_text = ROADMAPS.get(road_key, "Маршрут не определён")
    
    data = await state.get_data()
    vug_name = data.get('vug_name', '—')
    archetype_name = data.get('archetype_name', '—')
    professions = data.get('professions', '—')
    
    # Формируем итоговый отчёт
    report = (
        f"📋 ИТОГОВЫЙ ОТЧЁТ\n\n"
        f"Ваш профиль:\n"
        f"• ВУГ: {vug_name}\n"
        f"• Архетип: {archetype_name}\n\n"
        f"🎯 Целевые позиции:\n{professions}\n\n"
        f"🛤 Выбранный трек:\n{roadmap_text}\n\n"
        f"💡 Рекомендации по конвертации:\n"
    )
    
    for ex in CONVERSION_EXAMPLES:
        report += f"{ex}\n"
    
    report += (
        "\n✅ Первые шаги уже сегодня:\n"
        "1. Обновите резюме с учётом целевых позиций\n"
        "2. Изучите требования к интересующим вакансиям\n"
        "3. Запишитесь на профильные курсы\n"
        "4. Начните нетворкинг в профессиональном сообществе\n\n"
        "🎖 ПЛАН ПЕРЕХОДА СОСТАВЛЕН!\n\n"
        "Верьте в себя — вы нужны гражданской технологической индустрии!\n\n"
        "Для нового расчёта нажмите /start"
    )
    
    await callback.message.answer(report)
    
    # Очищаем состояние
    await state.clear()
    await callback.answer()