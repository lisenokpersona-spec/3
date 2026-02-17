# Пакет обработчиков для бота "Точка технологического перехода"
# Этот файл делает папку handlers импортируемым Python-пакетом

from . import start
from . import vug
from . import situations
from . import result
from . import roadmap

__all__ = ['start', 'vug', 'situations', 'result', 'roadmap']