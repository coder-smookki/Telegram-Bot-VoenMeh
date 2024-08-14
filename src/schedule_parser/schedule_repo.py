from datetime import date
import json

from redis import asyncio as aioredis
from redis.asyncio.client import Redis

from parser import parser
from config import (
    REDIS_HOST, REDIS_PORT,
    REDIS_EXPIRE_TIME,
    REDIS_GROUP_PREFIX, REDIS_PERIOD_KEY,
)
from exceptions import NotFoundGroupException


class ScheduleRepo:
    async def _set_data(self) -> None:
        redis_client = self._get_redis_client()
        json_data = await parser()

        await redis_client.set(
            REDIS_PERIOD_KEY,
            json.dumps(json_data["Timetable"]["Period"], ensure_ascii=False),
            ex=REDIS_EXPIRE_TIME,
        )
        for group_data in json_data["Timetable"]["Group"]:
            if group_data.get("Days") is None:
                continue
            group_name = group_data["@Number"]
            await redis_client.set(
                REDIS_GROUP_PREFIX + group_name,
                json.dumps(group_data, ensure_ascii=False),
                ex=REDIS_EXPIRE_TIME,
            )


    async def get_start_date(self) -> date:
        redis_client = self._get_redis_client()
        period_data = await self.get_data(REDIS_PERIOD_KEY, redis_client)

        period_data_json = json.loads(period_data)
        return date(
            int(period_data_json["@StartYear"]),
            int(period_data_json["@StartMonth"]),
            int(period_data_json["@StartDay"]),
        )


    async def get_group_data(self, group_name: str) -> list[dict]:
        """
        Args:
            group_name (str): Только верхни регистр и русские символы

        Raises:
            NotFoundGroupException: Если группа не найденна после обновления данных

        Returns:
            dict{
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
            }
        """
        redis_client = self._get_redis_client()
        group_data = await self.get_data(REDIS_GROUP_PREFIX + group_name, redis_client)
        if group_data is None:
            raise NotFoundGroupException
        return json.loads(group_data)


    async def get_data(self, key: str, redis_client: Redis) -> dict | list:
        data = await redis_client.get(key)
        if data is None:
            await self._set_data()
        return await redis_client.get(key)


    def _get_redis_client(self):
        return aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}")
