import asyncio

import aiohttp
import xmltodict

from config import SCHEDULE_URL


async def parser() -> dict:
    """Возвращает данные в практически сухом виде
    переводит xml в python dict

    Returns: # все данные в str (даже если это выглядит как число)
        dict: Timetable: {
            Weeks: {@WeekCount: "1" or "2" # четная/нечетная неделя}
            Period: {
                @Title: ВЕСЕННИЙ СЕМЕСТР 2023/2024 уч. г.
                @StartYear: 2024
                @StartMonth: 2
                @StartDay: 5
            }
            Group: [{
                @Number: О741Б
                @IdGroup: 3031
                Days: { 
                    Day: [{
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
                }
            }]
        }
    """
    params={'referrer': 'https://www.voenmeh.ru/trainee/timetable-stud'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0',
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'X-KL-kis-Ajax-Request': 'Ajax_Request',
        'Sec-GPC': '1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin'
    }
    session = aiohttp.ClientSession()
    async with session.get(SCHEDULE_URL, params=params, headers=headers) as response:
        response_content = await response.content.read()        
    await session.close()

    return xmltodict.parse(response_content)


if __name__ == "__main__": 
    asyncio.run(parser())