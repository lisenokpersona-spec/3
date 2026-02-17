from aiogram.fsm.state import State, StatesGroup

class TechTransition(StatesGroup):
    waiting_for_vug = State()
    waiting_for_archetype = State()
    waiting_for_situation_1 = State()
    waiting_for_situation_2 = State()
    waiting_for_situation_3 = State()
    waiting_for_situation_4 = State()
    waiting_for_situation_5 = State()
    waiting_for_roadmap = State()
