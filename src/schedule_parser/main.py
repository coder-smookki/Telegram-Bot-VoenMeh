from datetime import date

from schedule_repo import ScheduleRepo
from dataclass import DayScheduleData
from utils import get_week_code, get_str_weekday_by_index
from exceptions import NotFoundWeekdayException


async def get_day_schedule(group_name: str, day_date: date) -> DayScheduleData:
    """Возвращает расписание на день для группы, 
    с учетом четности текущей недели

    Args:
        group_name (str): Название группы (С УЧЕТОМ РЕГИСТРА) (НА РУССКОМ)
        day_date (date): Дата дня

    Raises:
        NotFoundGroupExceprion: not found group
        NotFoundWeekdayException: not found weekday

    Return: DayScheduleData
    """
    week_code = await get_week_code(day_date)
    weekday = get_str_weekday_by_index(day_date.weekday())
    
    group = await ScheduleRepo().get_group_data(group_name)
    
    week_schedule = group.schedule

    day_schedule = [i for i in week_schedule if i.weekday == weekday]
    if not day_schedule:
        raise NotFoundWeekdayException("Not found weekday")
    
    result = [i for i in day_schedule[0].lessons if i.week_code == week_code]

    return result


async def get_week_schedule(group_name: str, day_date: date) -> list[DayScheduleData]:
    """Возвращает расписание на неделю для группы, 
    с учетом четности текущей недели

    Args:
        group_name (str): Название группы (С УЧЕТОМ РЕГИСТРА) (НА РУССКОМ)
        day_date (date): Дата недели (подходит любой день)

    Raises:
        NotFoundGroupExceprion: not found group

    Return:
        list[DayScheduleData]
    """
    week_code = await get_week_code(day_date)

    group = await ScheduleRepo().get_group_data(group_name)
    
    for day_schedule in group.schedule:
        new_day_schedule = []
        for lesson in day_schedule.lessons:
            if lesson.week_code == week_code:
                new_day_schedule.append(lesson)
        day_schedule.lessons = new_day_schedule
    return group.schedule


async def get_two_weeks_schedule(group_name: str) -> list[DayScheduleData]:
    """Возвращает расписание на неделю для группы, 
    без учета четности текущей недели

    Args:
        group_name (str): Название группы (С УЧЕТОМ РЕГИСТРА) (НА РУССКОМ)
        week_code (str): "1" / "2" - нечетная/четная неделя

    Raises:
        NotFoundGroupExceprion: not found group

    Return:
        list[DayScheduleData]
    """
    group = await ScheduleRepo().get_group_data(group_name)
        
    return group.schedule