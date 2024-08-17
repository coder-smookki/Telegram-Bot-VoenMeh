from datetime import date

from parser_timetable.parser_engine.schedule_repo import ScheduleRepo
from parser_timetable.parser_engine.exceptions import SundayWorkDayException


async def get_week_code(current_date: date):
    """Вычисляет четность недели 
    из разницы между датой первой недели и current_date

    Args:
        current_date (date): Дата требуемого расписания

    Returns:
        str: "1" or "2"
    """
    start_date = await ScheduleRepo().get_start_date()
    return _get_week_code(start_date, current_date)
    

def _get_week_code(start_date: date, current_date: date) -> str:
    """Вычисляет разницу между start_date и current_date
    без учета дня недели, затем из этого вычисляется четность недели

    Args:
        start_date (date): Дата начала действия текущего комментария
        current_date (date): Дата требуемого расписания

    Returns:
        str: "1" or "2"
    """
    return str((
        ((current_date-start_date).days - current_date.weekday() + start_date.weekday()) 
        // 7) % 2 + 1
    )


def get_str_weekday_by_index(weekday_index: int) -> str:
    """Переводит числовое значение недели в строковое

    Args:
        weekday_index (int): число от 0 до 6 включительно

    Raises:
        SundayWorkDayException: в воскресенье пар нету

    Returns:
        str: День недели
    """
    if weekday_index == 6:
        raise SundayWorkDayException("Sunday is not a school day")
    
    weekdays_index = {
        0: "Понедельник", 1: "Вторник",
        2: "Среда", 3: "Четверг",
        4: "Пятница", 5: "Суббота",
    }
    return weekdays_index[weekday_index]