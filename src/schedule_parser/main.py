from datetime import date

from schedule_repo import ScheduleRepo
from utils import get_week_code, get_str_weekday_by_index
from exceptions import NotFoundWeekdayException


async def get_day_schedule(group_name: str, day_date: date) -> list[dict]:
    """Возвращает расписание на день для группы, 
    с учетом четности текущей недели

    Args:
        group_name (str): Название группы (С УЧЕТОМ РЕГИСТРА) (НА РУССКОМ)
        day_date (date): Дата дня

    Raises:
        NotFoundGroupExceprion: not found group
        NotFoundWeekdayException: not found weekday

    Return:
        list[{
            DayTitle: Понедельник # день недели
            WeekCode: "1" or "2" # четная/нечетная неделя
            Time: 9:00 Нечетная # Время начала пары и неделя
            Discipline: лек ПИТ. И С++ УЧИТЬ
            Lecturers: {
                IdLecturer: 6666
                ShortName: Иванов И.И.
            }
            Classroom: 666*;
        }]
    """
    week_code = await get_week_code(day_date)
    weekday = get_str_weekday_by_index(day_date.weekday())
    
    group = await ScheduleRepo().get_group_data(group_name)
    
    week_schedule = group["Days"]["Day"]

    day_schedule = [i for i in week_schedule if i["@Title"] == weekday]
    if not day_schedule:
        raise NotFoundWeekdayException("Not found weekday")
    
    result = [i for i in day_schedule[0]["GroupLessons"]["Lesson"] if i["WeekCode"] == week_code]

    return result


async def get_week_schedule(group_name: str, day_date: date) -> list[dict]:
    """Возвращает расписание на неделю для группы, 
    с учетом четности текущей недели

    Args:
        group_name (str): Название группы (С УЧЕТОМ РЕГИСТРА) (НА РУССКОМ)
        day_date (date): Дата недели (подходит любой день)

    Raises:
        NotFoundGroupExceprion: not found group

    Return:
        list[{
            @Title: Понедельник # день недели
            GroupLessons { 
                Lesson: [{
                    DayTitle: Понедельник # день недели
                    WeekCode: "1" or "2" # четная/нечетная неделя
                    Time: 9:00 Нечетная # Время начала пары и неделя
                    Discipline: лек ПИТ. И С++ УЧИТЬ
                    Lecturers: {
                        IdLecturer: 6666
                        ShortName: Иванов И.И.
                    }
                    Classroom: 666*;
                }]
            }
        }]
    """
    week_code = await get_week_code(day_date)

    group = await ScheduleRepo().get_group_data(group_name)
    
    week_schedule = group["Days"]["Day"]
    
    for day_schedule in week_schedule:
        new_day_schedule = []
        for lesson in day_schedule["GroupLessons"]["Lesson"]:
            if lesson["WeekCode"] == week_code:
                new_day_schedule.append(lesson)
        day_schedule["GroupLessons"]["Lesson"] = new_day_schedule
    return week_schedule


async def get_two_weeks_schedule(group_name: str) -> list[dict]:
    """Возвращает расписание на неделю для группы, 
    без учета четности текущей недели

    Args:
        group_name (str): Название группы (С УЧЕТОМ РЕГИСТРА) (НА РУССКОМ)
        week_code (str): "1" / "2" - нечетная/четная неделя

    Raises:
        NotFoundGroupExceprion: not found group

    Return:
        list[{
            @Title: Понедельник # день недели
            GroupLessons { 
                Lesson: [{
                    DayTitle: Понедельник # день недели
                    WeekCode: "1" or "2" # четная/нечетная неделя
                    Time: 9:00 Нечетная # Время начала пары и неделя
                    Discipline: лек ПИТ. И С++ УЧИТЬ
                    Lecturers: {
                        IdLecturer: 6666
                        ShortName: Иванов И.И.
                    }
                    Classroom: 666*;
                }]
            }
        }]
    """

    group = await ScheduleRepo().get_group_data(group_name)
    
    week_schedule = group["Days"]["Day"]
    
    return week_schedule


if __name__ == "__main__":
    import pprint
    import asyncio
    pprint.pprint(asyncio.run(get_week_schedule("А121С", date(2024, 8, 18))))